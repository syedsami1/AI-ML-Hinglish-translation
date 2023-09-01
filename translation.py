# translation.py

import re

def selective_hinglish_translate(text):
    # Define a translation dictionary for specific words
    translation_dict = {
        "definitely": "बिल्कुल",
        "share": "शेयर",
        "feedback": "प्रतिक्रिया",
        "mention": "उल्लेख",
        "products": "उत्पाद",
        "video": "वीडियो",
        "minute": "मिनट",
        "headset": "हेडसेट",
        "bag": "बैग",
    }

    # Use regex to find and translate specific words
    pattern = re.compile(r'\b(?:' + '|'.join(re.escape(word) for word in translation_dict.keys()) + r')\b')
    
    def translate_word(match):
        return translation_dict.get(match.group(0).lower(), match.group(0))

    translated_text = pattern.sub(translate_word, text)

    return translated_text
