import openai
openai.api_key = "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"

def correct_spelling(input_text):
    prompt = "Correct the spelling of the following text: '{}'".format(input_text)
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=100,
        n=1,
        temperature=0.8
    )
    output_text = response.choices[0].text.strip()
    if not output_text.startswith(input_text):
        # If the model doesn't correct the input text, return the original text
        return input_text
    else:
        # Extract the corrected text from the output
        corrected_text = output_text[len(input_text)+1:][:-1]
        return corrected_text