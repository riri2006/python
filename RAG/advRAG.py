from langchain_groq import ChatGroq
from llama_cloud import LlamaCloud
from langchain_core.documents import Document
from langchain_experimental.text_splitter import SemanticChunker
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain.agents import create_agent
from langgraph.checkpoint.memory import MemorySaver
from pathlib import Path
import os
from dotenv import load_dotenv
load_dotenv()

class Assistant:
    def __init__(self,name,ai):
        self.ai= ai
        self. name = name

    def assistant(self):
        llm = ChatGroq(model="openai/gpt-oss-20b")
        memory = MemorySaver()
        agent = create_agent(
            model=llm,
            checkpointer=memory
        )

        path = input("Enter the path of file: ")

        #----------------------------------------CLOUD-----------------------------------------
        client = LlamaCloud(
            api_key=os.getenv("LLAMA_CLOUD_API_KEY"),
            timeout=120.0)

        file = client.files.create(
            file=Path(path),
            purpose="parse")

        result = client.parsing.create(
            tier="agentic",
            version="latest",
            file_id=file.id)

        parsed = client.parsing.get(
            result.id,
            expand="markdown" )
        
        documents = []
        for doc in parsed.markdown.pages:
            documents.append(
                Document(
                    page_content=doc.markdown,
                    metadata={"source":path}
                )
            )

        embedding = OllamaEmbeddings(model="nomic-embed-text:latest")
        splitter = SemanticChunker(embeddings=embedding)

        chunks = splitter.split_documents(documents)

        vdb = Chroma.from_documents(
            documents=chunks,
            embedding= embedding,
            persist_directory="./advncrag_db"
        )

        while True:
            query = input(f"\n{self.name}: ")
            if query.lower() in ["exit", "quit", "terminate"]:
                print("Terminating conversation.. Thank you")
                break

            response = vdb.similarity_search(
                query= query,
                k=5,
                filter={"source":path}
            )
            context = "\n\n".join(
                    doc.page_content
                    for doc in response)
                        
            prompt = f"""
                You are {self.ai} a helpful multimodal document assistant.

                You answer questions about the uploaded document, which may contain
                text, images, scanned pages, charts, diagrams, tables, logos, and other
                visual content.

                Use the document context below whenever it is relevant.

                Document context:
                {context}

                Current question:
                {query}

                Rules:

                1. If the answer is available in the document text or context, answer using it.
                and  If the user asks "what does it mean?", "explain this",
                "what is the message?", or asks for interpretation,
                explain the meaning of the text or visual content
                in simple language.

                2. If the question is about visual content in the uploaded document,
                such as:
                - colors
                - objects
                - people or animals
                - number of objects
                - logos or symbols
                - charts or diagrams
                - shapes
                - images
                - visual layout
                - appearance or position of elements

                use the visual information from the uploaded document to answer.

                3. If the document contains both text and visual information, combine
                both when necessary to answer the question.

                4. Do not assume that all information in an image is present in the
                extracted text. Visual questions may require analyzing the actual image.

                5. If the exact answer is NOT available from the document or its visual
                content, but the question is related to the same topic, you may answer
                using general knowledge.

                6. If the question is completely unrelated to the uploaded document,
                say:

                "I could not find this information."

                7. Do not invent or hallucinate visual details. If you cannot determine
                something from the available document content, clearly say that you
                cannot determine it.

                8. Do not mention how many times a sentence, paragraph, fact,
                or piece of information is repeated in the document.
                Do not discuss duplicate or repeated content unless the user
                specifically asks about repetition or frequency.

                9. Give simple, clear, and direct answers.
                """
            result = agent.invoke({
                    "messages":[{"role":"user","content":prompt}]
            }, config={"configurable":{"thread_id":"1"}})

            print(f"\n{self.ai} ", result['messages'][-1].content)
            
            
