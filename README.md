# 🤖 Build Your First AI Agent in Under 100 Lines of Python

Have you ever wondered how AI agents actually work?

This project demonstrates the **core concepts behind an AI agent** in fewer than **100 lines of Python**. Instead of relying on large frameworks or paid APIs, you'll build a simple AI agent that can decide when to use tools, execute Python functions, and generate intelligent responses using a local Hugging Face language model.

The best part?

- Less than 100 lines of Python
- No API key required
- Beginner-friendly
- Runs perfectly in **Google Colab** or **Jupyter Notebook**
.Whether you're new to AI or just curious about how AI agents work behind the scenes, this project is a great place to start.
---

# Features

- Runs a local Hugging Face language model
- Includes a calculator tool
- Includes a mock system status tool
- Demonstrates AI tool calling
- No OpenAI API required
- Easy to understand and modify
- Easily swap between different Hugging Face models

---

# Technologies Used

- Python
- Hugging Face Transformers
- PyTorch
- Accelerate

---

# 🚀 Getting Started

This project is designed to be as beginner-friendly as possible.

Instead of setting up a full Python project, simply copy the code into one of the following environments:

- **Google Colab** ⭐ *(Recommended)*
- **Jupyter Notebook**

Both environments allow you to run the project one cell at a time, making it easy to experiment, modify the code, and understand how each part of the AI agent works.

---

# Step 1: Install the Dependencies

Run the following command in your first notebook cell:

```python
!pip install -q transformers accelerate torch
```

This installs all of the libraries required for the AI agent.

---

# Step 2: Copy the Code

Copy the complete Python code from this repository into a new notebook cell.

Then simply run the cell.

The first time you execute the notebook, Hugging Face will automatically download the language model. Depending on your internet connection, this may take a minute or two.

After the initial download, the model will be cached locally, making future runs significantly faster.

---

# ▶️ Example Output

```text
User:
What is 45 * 12 + 8?

Agent Calling Tool:
calculate(45*12+8)

Tool Output:
548

Agent Answer:
The result of 45 × 12 + 8 is 548.
```

---


# 🔧 Available Tools

## Calculator

```python
calculate(expression)
```

Example:

```python
calculate(45 * 12 + 8)
```

---

##  System Status

```python
get_system_status()
```

Example output:

```text
All local systems operational.
Battery: 88%.
```

---

# Try Different Language Models

One of the best things about using Hugging Face is that you can experiment with different AI models by changing **just one line of code**.

Current model:

```python
model_id = "Qwen/Qwen2.5-0.5B-Instruct"
```

Try one of these instead:

```python
model_id = "meta-llama/Llama-3.2-1B-Instruct"
```

```python
model_id = "google/gemma-3-1b-it"
```

```python
model_id = "microsoft/Phi-3.5-mini-instruct"
```

```python
model_id = "HuggingFaceTB/SmolLM2-1.7B-Instruct"
```

Simply replace the `model_id`, rerun the notebook, and compare how each model responds.

---

# Accompanying Technical Blog

This repository accompanies my technical article:

> **Build Your First AI Agent in Under 100 Lines of Python (Explained Like We're Building It Together)**: https://evapatel123.hashnode.dev/your-basic-ai-agent-in-100-lines-of-python-explained-like-we-re-building-it-together

The article walks through the project **line by line**, explaining every piece of code in beginner-friendly language and showing how AI agents actually work behind the scenes.

---

# Contributing

Contributions are always welcome!

If you have ideas for new tools, improvements, optimizations, or bug fixes, feel free to open an issue or submit a pull request.

Happy coding! 
