# Parallel-AI-Agents
A framework designed to orchestrate, manage, and execute multiple AI agents in parallel.

# Parallel AI Agents (News Aggregator) 🤖📰

A Python framework designed to orchestrate, manage, and execute multiple AI agents in parallel using Google's Agent Development Kit (ADK) and `LiteLlm`. 

This specific project demonstrates a parallel multi-agent system that simultaneously fetches and aggregates updates across three distinct domains: Cricket News, Weather Forecasts, and Stock Market updates.

---

## 🚀 Features & Architecture

* **Parallel Execution:** Uses `ParallelAgent` to invoke multiple sub-agents concurrently, drastically reducing total latency.
* **Specialized Sub-Agents:**
  * **Cricket Agent:** A dedicated specialist delivering concise cricket news and sports updates.
  * **Weather Agent:** A localized specialist providing quick weather updates and forecasts.
  * **Stock Agent:** A financial specialist supplying key stock market trends and news.
* **Isolated Output Keys:** Each agent maps its output safely using unique keys (`cricket_news`, `weather_news`, `stock_news`) to avoid payload conflicts.

---

## 🛠️ Tech Stack

* **Language:** Python
* **Framework:** Google Agent Development Kit (ADK)
* **LLM Orchestration:** `LiteLlm`
* **Underlying Model:** `groq/llama-3.3-70b-versatile`

---

## 💻 Code Overview

The core system architecture sets up three independent `LlmAgent` instances wrapped inside a single `ParallelAgent` root coordinator:

```python
from google.adk.agents import LlmAgent, SequentialAgent, ParallelAgent
from google.adk.models.lite_llm import LiteLlm

# Initialize Model via LiteLlm
model = LiteLlm(model="groq/llama-3.3-70b-versatile")

# Define Specialized Agents
cricket_agent = LlmAgent(
    name="cricket_agent",
    model=model,
    instruction="You are a cricket news specialist. Provide the latest cricket news and updates in a concise format.",
    output_key="cricket_news",
)

weather_agent = LlmAgent(
    name="weather_agent",
    model=model,
    instruction="You are a weather news specialist. Provide the latest weather updates and forecasts in a concise format.",
    output_key="weather_news",
)

stock_agent = LlmAgent(
    name="stock_agent",
    model=model,
    instruction="You are a stock market news specialist. Provide the latest stock market news and updates in a concise format.",
    output_key="stock_news",
)

# Parallel orchestration layer
root_agent = ParallelAgent(
    name="news_aggregator",
    sub_agents=[cricket_agent, weather_agent, stock_agent],
)
