import openai
import os

# Get the API key from the environment variable
api_key = os.getenv('OPENAI_API_KEY')

# Set up the OpenAI API credentials
openai.api_key = api_key

# Initialize the conversation history list
conversation_history = []

# Define the initial prompt for the conversation
initial_prompt = input("Enter the initial prompt: ")
conversation_history.append(initial_prompt)

while True:
    # Join the conversation history prompts into a single string
    conversation_prompt = '\n'.join(conversation_history)

    # Call the OpenAI API to generate a response
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=conversation_prompt,
        max_tokens=100
    )

    # Get the generated response
    generated_response = response.choices[0].text.strip()

    # Store the generated response in the conversation history
    conversation_history.append(generated_response)

    # Print the generated response
    print(generated_response)

    # Ask the user for the next prompt
    next_prompt = input("Enter your next prompt (or 'q' to quit): ")

    if next_prompt.lower() == 'q':
        break

    # Add the user's prompt to the conversation history
    conversation_history.append(next_prompt)
