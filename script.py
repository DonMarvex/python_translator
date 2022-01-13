from translate import Translator
# Import Translator module from translate package

translator = Translator(to_lang='ja')
# Set translation language to Japanese

# Keep code in a try except block and catch FileNotFoundError
# Write translated text to a new file

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
