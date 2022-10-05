import googletrans
from googletrans import Translator

print(googletrans.LANGUAGES)

text1 = "Hello welcome to my website!"
translator = Translator()
ln=translator.detect(text1)
print(ln.lang)
trans1 = translator.translate(text1, src='en', dest='ja')

print("English to Japanese: ", trans1.text)
