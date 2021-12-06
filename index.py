import paho.mqtt.client as mqtt
import subprocess
from applescript import tell
import pyttsx3
engine = pyttsx3.init()

# The callback for when the client receives a CONNACK response from the server.


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("mybot/mymac/controls")

# The callback for when a PUBLISH message is received from the server.


def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    message = msg.payload = msg.payload.decode("utf-8")
    print(message)
    if(message == "shutdown"):
        print("shutdown my mac")
        engine.say(message)
        engine.runAndWait()
        subprocess.call(
            ['osascript', '-e', 'tell app "loginwindow" to «event aevtrsdn»'])
    elif(message == "lock"):
        subprocess.Popen('ls -la', shell=True)
    elif(message == "delete"):
        engine.say(message)
        engine.runAndWait()
        subprocess.run(
            'rm /Users/dicksen.veloopillay/test_folder/*.py', shell=True)
    elif(message == "go to facebook"):
        engine.say(message)
        engine.runAndWait()
        subprocess.Popen(['open', 'https://www.facebook.com'])
    elif(message == "go to youtube"):
        engine.say(message)
        engine.runAndWait()
        subprocess.Popen(
            ['open', 'https://www.youtube.com/watch?v=w39_DAZHFVA'])
    elif(message == "hack"):
        yourCommand = 'echo you have been hacked copying all you files........'
        tell.app('Terminal', 'do script "' + yourCommand + '"')
    else:
        print('else')
        engine.say(message)
        engine.runAndWait()


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipseprojects.io", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.

client.loop_forever()
