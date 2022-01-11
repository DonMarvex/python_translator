from translate import Translator

translator = Translator(to_lang='ja')

try:
    with open('C:/Users/Marvel/Desktop/test.txt', mode='r') as my_file:
        print('File loaded')
        text = my_file.read()
        translation = translator.translate(text)
        print(translation)
        with open('C:/Users/Marvel/Desktop/test-ja.txt', mode='w') as my_file2:
            my_file2.write(translation)
except FileNotFoundError as err:
    print('File does not exist')
    raise err
