from openai import OpenAI

client = OpenAI()

def open_url_and_fetch_content(url):
    # This function would handle the HTTP request to fetch the content from the URL
    import requests
    response = requests.get("https://platform.openai.com/docs/api-reference")
    return response.text

# Create an Assistant with function calling enabled
assistant = client.assistants.create(
    model="gpt-4.0",
    instructions="This assistant can call functions to open URLs and fetch content.",
    tools=[{"type": "code_interpreter"}]
)

# Define the function for the Assistant to use
assistant.tools.code_interpreter.functions["fetch_api_docs"] = open_url_and_fetch_content

# Call the function through the Assistant
tool_call_response = client.tool_calls.create(
    assistant_id=assistant.id,
    tool_call={
        "tool_name": "code_interpreter",
        "function_name": "fetch_api_docs",
        "parameters": {"url": "https://platform.openai.com/docs/api-reference"}
    }
)

print(tool_call_response.outputs["result"])
