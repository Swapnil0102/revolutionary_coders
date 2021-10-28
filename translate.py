from googletrans import Translator

def translate(string):
    return 0

if __name__ == '__main__':
    translator = Translator()
    ar = translator.translate('مرحبا').text
    print(ar)