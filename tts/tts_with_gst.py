import speech_recognition as sr
from gtts import gTTS
import os
import gi
gi.require_version('Gst', '1.0')
from gi.repository import GObject, Gst
import tempfile
import sys
import threading
import time

playbin = None
loop = None
playlist = []

def check_next():
    if len(playlist):
        filename = playlist[0]
        play_sound( filename )
        playlist.remove( filename )
        if Gst.uri_is_valid(filename):
            uri = args[1]
        else:
            uri = Gst.filename_to_uri(filename)
        playbin.set_property('uri', uri)

        playbin.set_state(Gst.State.PLAYING)

def bus_call(bus, message, loop):
    t = message.type
    if t == Gst.MessageType.EOS:
        check_next()
    elif t == Gst.MessageType.ERROR:
        err, debug = message.parse_error()
        sys.stderr.write("Error: %s: %s\n" % (err, debug))
        loop.quit()
    return True

def play_sound(filename):
    global playbin

    print("Play_sound :", filename)

    if not playbin:
        playbin, loop = init()

    state = playbin.get_state(Gst.State.NULL)
    if state.state == Gst.State.PLAYING:
        print("Add To List :", filename)
        playlist.append(filename)
        return
    elif state.state == Gst.State.READY:
        print("Ready")
    elif state.state == Gst.State.PAUSED:
        print("Paused")
    elif state.state == Gst.State.NULL:
        print("Null")
    else:
        print("Unknown State")
        print(state)

    # take the commandline argument and ensure that it is a uri
    if Gst.uri_is_valid(filename):
      uri = args[1]
    else:
      uri = Gst.filename_to_uri(filename)
    playbin.set_property('uri', uri)

    playbin.set_state(Gst.State.PLAYING)

def speak(text):
    fd, filename = tempfile.mkstemp()
    try:
        tts = gTTS(text=text, lang='ko')
    except ConnectionError:
        print("Connection Error")
        return
    tts.save(filename)
    play_sound(filename)

def init():
    GObject.threads_init()
    Gst.init(None)

    playbin = Gst.ElementFactory.make("playbin", None)
    if not playbin:
        sys.stderr.write("'playbin' gstreamer plugin missing\n")
        sys.exit(1)

    # create and event loop and feed gstreamer bus mesages to it
    loop = GObject.MainLoop()

    bus = playbin.get_bus()
    bus.add_signal_watch()
    bus.connect ("message", bus_call, loop)

    play_thread = threading.Thread(target=loop.run, daemon=True)
    play_thread.start()

    return playbin, loop

def main():
    global playbin, loop, playlist

    playbin, loop = init()
    speak("안녕하세요.")
    speak("저는 뽁스입니다.")

    try:
        while True:
            check_next()
            print(".")
            time.sleep(1)
    except KeyboardInterrupt:
        exit(0)
    
if __name__ == '__main__':
    main()

