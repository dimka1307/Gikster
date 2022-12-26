import paho.mqtt.client as mqtt
import time
from datetime import datetime

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")


def main(s1,s2,s3,p):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    client = mqtt.Client()
    client.on_connect = on_connect
    client.connect("broker.emqx.io", 1883, 60)
    client.loop_start()
    client.publish('Proekt/sharzeri', payload= str(s1) + " " + str(s2) + " " + str(s3), qos=2, retain=True)
    client.publish('Proekt/promet', payload= current_time + " " + str(p) + " den", qos=2, retain=True)
    time.sleep(5)
    client.loop_stop()


if __name__ == "__main__":
    main()
