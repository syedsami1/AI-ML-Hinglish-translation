# main.py

from translation import selective_hinglish_translate

if __name__ == "__main__":
    # Get the English text to translate.
    text_list = [
        "Definitely share your feedback in the comment section.",
        "So even if it's a big video, I will clearly mention all the products.",
        "I was waiting for my bag."
    ]

    print("Original Texts:")
    for text in text_list:
        print(text)

    print("\nTranslated Texts:")
    for text in text_list:
        # Translate the text to Hinglish with selective word translation.
        hinglish_text = selective_hinglish_translate(text)
        print(hinglish_text)
