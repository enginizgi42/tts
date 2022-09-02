from gtts import gTTS    #library for Google Text-to-Speech
import os       #to open audio file automatically after its created
print("text ismini giriniz:")
text=input()
f = open(text +".txt")

#text = "Hello world"
text = f.read()
language = "tr"
print("mp3 ismini giriniz:")
obj = gTTS(text = text, lang= language, slow=False)
isim= input()
obj.save( isim +".mp3")
print("mp3 dosyası hazır")
#os.system("samle.mp3")     #to launch mp3 player after conversion is done
