# main.py
import qi

session = qi.Session()

robot = session.connect("tcp://<ROBOT_IP>:9559")

tts = session.service("ALTextToSpeech")
tts.say("Hello, world!")