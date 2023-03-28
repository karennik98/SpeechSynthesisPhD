import openai
openai.api_key = "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"

def correct_sentence(sentence):
    prompt = f"Please correct only the punctuation and spelling errors in the following text: {sentence}"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    corrected_sentence = response.choices[0].text.strip()
    return corrected_sentence
