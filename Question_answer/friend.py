import pyttsx3
friend = pyttsx3.init()
speech = input("Hello guys : ")
friend.say(speech)
friend.runAndWait()
