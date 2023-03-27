import openai
openai.api_key = "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"

def correct_sentence(sentence):
    prompt = f"Please correct the following sentence: {sentence}"
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
