from deep_translator import GoogleTranslator


def translation(text):
    """
    Using the Google Translator
    GoogleTranslator is the free/unofficial Google Translate, not the official Google Cloud API.
    """
    return GoogleTranslator(source='auto', target='en').translate(text)


if __name__ == '__main__':
    text = str(input("Please enter an arbitrary text for translation (stop to terminate): "))
    while text != "stop":
        print(translation(text))
        text = str(input("Please enter text: "))
    print("Program terminated ...")




