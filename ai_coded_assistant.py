import openai
from openai import OpenAI

# Initialize the OpenAI client
apikey = "sk-proj-qfhKKD6FKpyM6qRJWx71T3BlbkFJLGnuqOyji8v965kWayuM"

client = OpenAI(api_key=apikey)


# Step 1: Create an Assistant with File Search Enabled
assistant = client.beta.assistants.create(
    name="Financial Analyst Assistant",
    description="You are an expert financial analyst. Use your knowledge base to answer questions about audited financial statements.",
    model="gpt-4o",
    tools=[{"type": "file_search"}]
)

# Print Assistant ID
print(f"Assistant ID: {assistant.id}")

# Step 2: Upload files and add them to a Vector Store
vector_store = client.beta.vector_stores.create(name="Financial Statements")
file_paths = ["edgar/goog-10k.pdf", "edgar/brka-10k.txt"]
file_streams = [open(path, "rb") for path in file_paths]
file_batch = client.beta.vector_stores.file_batches.upload_and_poll(
    vector_store_id=vector_store.id, files=file_streams
)

# Print Vector Store ID
print(f"Vector Store ID: {vector_store.id}")

# Step 3: Update the assistant to use the new Vector Store
assistant = client.beta.assistants.update(
    assistant_id=assistant.id,
    tool_resources={"file_search": {"vector_store_ids": [vector_store.id]}}
)

# Step 4: Create a Thread
message_file = client.files.create(
    file=open("edgar/aapl-10k.pdf", "rb"), purpose="assistants"
)
thread = client.beta.threads.create(
    messages=[
        {
            "role": "user",
            "content": "How many shares of AAPL were outstanding at the end of October 2023?",
            "attachments": [
                {"file_id": message_file.id, "tools": [{"type": "file_search"}]}
            ],
        }
    ]
)

# Print Thread ID
print(f"Thread ID: {thread.id}")

# Step 5: Create a Run and check the output
from openai import AssistantEventHandler

class EventHandler(AssistantEventHandler):
    def on_text_created(self, text) -> None:
        print(f"\nassistant > {text}", end="", flush=True)

    def on_tool_call_created(self, tool_call):
        print(f"\nassistant > {tool_call.type}\n", flush=True)

    def on_message_done(self, message) -> None:
        message_content = message.content[0].text
        annotations = message_content.annotations
        citations = []
        for index, annotation in enumerate(annotations):
            message_content.value = message_content.value.replace(
                annotation.text, f"[{index}]"
            )
            if file_citation := getattr(annotation, "file_citation", None):
                cited_file = client.files.retrieve(file_citation.file_id)
                citations.append(f"[{index}] {cited_file.filename}")
        print(message_content.value)
        print("\n".join(citations))

with client.beta.threads.runs.stream(
    thread_id=thread.id,
    assistant_id=assistant.id,
    instructions="Please address the user as Jane Doe. The user has a premium account.",
    event_handler=EventHandler(),
) as stream:
    stream.until_done()
