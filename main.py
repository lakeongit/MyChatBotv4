import openai
import speech_recognition as sr
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

# Initialize the speech recognizer
recognizer = sr.Recognizer()

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

    # Ask the user for the next prompt or listen for speech input
    next_input = input("Enter your next prompt or type 's' to start speech recognition (or 'q' to quit): ")

    if next_input.lower() == 'q':
        break

    if next_input.lower() == 's':
        print("Listening...")

        # Use speech recognition to listen for audio input
        with sr.Microphone() as source:
            audio = recognizer.listen(source)

        try:
            # Recognize speech from the audio input
            speech_input = recognizer.recognize_google(audio)
            print("Speech Input:", speech_input)

            # Add the speech input to the conversation history
            conversation_history.append(speech_input)
        except sr.UnknownValueError:
            print("Speech recognition could not understand audio.")
        except sr.RequestError as e:
            print("Could not request results from speech recognition service; {0}".format(e))
    else:
        # Add the user's prompt to the conversation history
        conversation_history.append(next_input)
