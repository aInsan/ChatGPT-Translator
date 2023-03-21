import openai

openai.api_key = "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"


def translate_text(input_language, text, target_language):
    prompt = f"Translate '{text}' form '{input_language}'to {target_language}:"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
  )
    return response.choices[0].text.strip()


def ask_question():
    input_language = input("What language are you typing in?: ")
    text = input("Type your text: ")
    target_language = input("Type your target language: ")

    translated_text = translate_text(input_language, text, target_language)

    print(translated_text)

    do_continue = input("T to continue Q to quit: ")
    if do_continue == "T":
        ask_question()


ask_question()
