import paho.mqtt.client as mqtt
import subprocess


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("mybot/controls")

# The callback for when a PUBLISH message is received from the server.


def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    message = msg.payload = msg.payload.decode("utf-8")
    print(message)
    if(message == "left"):
        print("lock my screen")
        subprocess.call(
            ['osascript', '-e', 'tell app "loginwindow" to «event aevtrsdn»'])


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("mqtt.eclipseprojects.io", 1883, 60)


client.loop_forever()
