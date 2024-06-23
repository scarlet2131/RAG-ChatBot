# Load OpenAI credentials
import json
from openai import OpenAI

from app.core.config import settings

openai_api_key = settings.OPENAI_API_KEY
client = OpenAI(api_key=openai_api_key)


def generate_prompt(user_input, relevant_docs):
    prompt = f"""
            User query: {user_input}

            Use the following relevant information to provide a detailed and contextually accurate response:

            {relevant_docs}

            If the relevant information does not address the query directly, or if the user query is a general question or greeting (e.g., "hi", "how's the weather"), respond appropriately without referencing the document.
            
            Also you are replying to the user do not mention any internal implementaion like do not mention the document information just give the final response without mentioning the internal details.
            """

    # prompt = f"User query: {user_input}\n\nRelevant document: {relevant_docs}\n\nProvide a detailed response based on the relevant document if anything found else just reply based on user input alone:"
    return prompt

def get_response_with_chatgpt(user_input: str, relevant_docs: str) -> dict:

    try:
        # Assume generate_prompt(text) correctly generates the detailed prompt as before
        prompt_text = generate_prompt(user_input, relevant_docs)
        print("promt - text   ", prompt_text)

        # Make the API call
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=[
                {"role": "user", "content": "You are a helpful assistant designed to output JSON."},
                {"role": "user", "content": prompt_text}
            ]
        )
        # Extract the response text
        response_text = response.choices[0].message.content.strip()
        print("Response - text:", response_text)

        # Check if response_text is valid JSON
        try:
            response_data = json.loads(response_text)
        except json.JSONDecodeError:
            response_data = {"response": response_text}

        # Return the parsed dictionary or plain text response
        return response_data

    #     # Extract the response text
    #     response_text = response.choices[0].message.content.strip()
    #     print("response - text   ", response_text)
    #
    #
    #     # Parse the JSON string into a Python dictionary
    #     response_data = json.loads(response_text)
    #
    #     # Return the parsed dictionary
    #     return response_data
    except Exception as e:
        print("Error:", e)
        return {}

