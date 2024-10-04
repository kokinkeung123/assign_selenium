from gtts import gTTS
import os

text = 'assignment 課程名稱: Python 網站框架開發助理證書 課程編號 : CT290DS 姓名 : 高健強 班號 : 16'


# save file to Cantonese Speech
tts = gTTS(text=text, lang='yue')
tts.save("readme.mp3")
# Speech
os.system("mpg321 readme.mp3")
