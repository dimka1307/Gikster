import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")

def on_message(client, userdata, message):
    print("Recieved message: ", str(message.payload.decode("utf-8")))
    global cena
    cena = message.payload.decode("utf-8")
    
def main():
    client = mqtt.Client("Raspberry Pi")
    client.on_connect = on_connect
    client.connect("broker.emqx.io", 1883, 60)
    client.loop_start()
    client.subscribe("Proekt/cena")
    client.on_message = on_message
    time.sleep(5)
    client.loop_stop()
    return cena


if __name__ == "__main__":
    main()
