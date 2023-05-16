import openai
openai.api_key = "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"
response = openai.Completion.create(
    engine='text-davinci-003',  # Specify the engine to use (e.g., text-davinci-003)
    prompt='Hello, how can I help you?',  # Provide a conversation prompt or message
    max_tokens=50  # Set the maximum number of tokens in the response
)

reply = response.choices[0].text.strip()  # Extract the generated reply from the response
print(reply)