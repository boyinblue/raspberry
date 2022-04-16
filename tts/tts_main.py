import tts
import tts_datetime

menu_item = ["오늘 날짜",
                "현재 시간",
                "음악" ]

menu = None

def parse_key(key):
    if key == "KEY_MENU" and not menu:
        tts.speak("메뉴")
        for i in range(len(menu_item)):
            tts_msg = "{}번 {}".format(i, menu_item[i])
            tts.speak(tts_msg)
    elif key == "KEY_0":
        tts_datetime.play_date()
    elif key == "KEY_1":
        tts_datetime.play_time()

def main():
    pass

if __name__ == '__main__':
    main()
