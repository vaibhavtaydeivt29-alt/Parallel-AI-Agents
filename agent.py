from google.adk.agents import LlmAgent, SequentialAgent, ParallelAgent
from google.adk.models.lite_llm import LiteLlm

model = LiteLlm(model="groq/llama-3.3-70b-versatile")

# cricket news agent
cricket_agent = LlmAgent(
    name="cricket_agent",
    model=model,
    instruction="You are a cricket news specialist. Provide the latest cricket news and updates in a concise format.",
    output_key="cricket_news",
)

# weather news agent
weather_agent = LlmAgent(
    name="weather_agent",
    model=model,
    instruction="You are a weather news specialist. Provide the latest weather updates and forecasts in a concise format.",
    output_key="weather_news",
)
# stock market news agent
stock_agent = LlmAgent(
    name="stock_agent",
    model=model,
    instruction="You are a stock market news specialist. Provide the latest stock market news and updates in a concise format.",
    output_key="stock_news",
)

# parallel agent to run all three agents simultaneously
root_agent = ParallelAgent(
    name="news_aggregator",
    sub_agents=[cricket_agent, weather_agent, stock_agent],
)