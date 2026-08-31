from langchain_groq import ChatGroq
from llama_cloud import LlamaCloud
from langchain.agents import create_agent
from langgraph.checkpoint.memory import MemorySaver
from pathlib import Path
import os
import time
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model="openai/gpt-oss-20b")

memory = MemorySaver()

agent = create_agent(
    model=llm,
    checkpointer=memory
)

path = input("Enter the path of file: ")

# ---------------------------------------- CLOUD -----------------------------------------

client = LlamaCloud(
    api_key=os.getenv("LLAMA_CLOUD_API_KEY"),
    timeout=120.0
)

file = client.files.create(
    file=Path(path),
    purpose="parse"
)

result = client.parsing.create(
    tier="agentic",
    version="latest",
    file_id=file.id
)

# Wait until parsing is completed
while True:
    parsed = client.parsing.get(
        result.id,
        expand="markdown"
    )

    if parsed.job.status == "COMPLETED":
        break

    time.sleep(2)

# Print Markdown
for page in parsed.markdown.pages:
    print(page.markdown)