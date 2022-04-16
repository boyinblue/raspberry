import speech_recognition as sr
from gtts import gTTS
import os
import playsound
import tempfile

def speak(text):
    fd, filename = tempfile.mkstemp()
    tts = gTTS(text=text, lang='ko')
    tts.save(filename)
    playsound.playsound(filename)
    os.unlink(filename)

def main():
    speak("안녕하세요. 저는 박선우입니다.")
    speak("안녕하세요. 박선우")
    speak("똥 나와요. 박세진")
    speak("똥 나왔어요. 박서준")
    speak("똥 나와요. 신미현")
    speak("똥 나와요. 아저씨")
    speak("너무 냄새나요 똥")
    speak("옛날 옛적에 응가 박사가 살았어요. 응가 박사는 한 번에 응가를 1톤씩은 싸곤 했어요. 그러던 어느 날, 다른 나라에서 방구 대장이 쳐들어 왔어요. 응가 박사는 방구 대장에 맞서서 열심히 싸웠어요.")

if __name__ == '__main__':
    main()

