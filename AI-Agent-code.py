# NOTE: Make sure you run this code in a different google colab cell before running the below code: !pip install -q transformers accelerate torch

import math, re
from transformers import pipeline

# 1. Load a fast local model (No API Key required)
model_id = "Qwen/Qwen2.5-0.5B-Instruct" # Feel free to experiment with different Hugging Face Models
agent_llm = pipeline("text-generation", model=model_id, max_new_tokens=100)

# 2. Define tools available to the agent
def calculate(expr: str) -> str:
    try:
        return str(eval(expr, {"__builtins__": None, "math": math}))
    except Exception as e:
        return f"Error: {e}"

def get_system_status() -> str:
    return "All local systems operational. Battery: 88%."

TOOLS = {"calculate": calculate, "get_system_status": get_system_status}

# 3. Agent System Prompt defining available tools
SYSTEM_PROMPT = """You are an AI Agent with tool access.
Tools available:
- calculate(expression)
- get_system_status()

If you need a tool, reply in this exact format:
TOOL: <tool_name>(<arguments>)

Otherwise, answer directly.
"""

# 4. Agent Loop
def run_agent(query: str):
    print(f"\n User: {query}")
    prompt = f"<|im_start|>system\n{SYSTEM_PROMPT}<|im_end|>\n<|im_start|>user\n{query}<|im_end|>\n<|im_start|>assistant\n"

    # Step A: Model generates response or tool call request
    output = agent_llm(prompt, return_full_text=False)[0]["generated_text"].strip()

    # Step B: Parse and execute tool if requested
    if output.startswith("TOOL:"):
        tool_call = output.replace("TOOL:", "").strip()
        print(f"Agent Calling Tool: {tool_call}")

        if "calculate" in tool_call:
            expr = re.findall(r"\((.*?)\)", tool_call)[0]
            result = calculate(expr)
        elif "get_system_status" in tool_call:
            result = get_system_status()
        else:
            result = "Unknown tool"

        print(f"Tool Output: {result}")

        # Step C: Pass tool result back to the model for final answer
        final_prompt = prompt + f"{output}\n<|im_start|>user\nTool Output: {result}<|im_end|>\n<|im_start|>assistant\n"
        final_response = agent_llm(final_prompt, return_full_text=False)[0]["generated_text"].strip()
        print(f"Agent Answer: {final_response}")
    else:
        print(f"Agent Answer: {output}")

# Run tests
run_agent("What is 45 * 12 + 8?")
run_agent("What universities are famously known for their computer science major?")
