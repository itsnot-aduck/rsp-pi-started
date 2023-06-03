import random
import time
import  sys
from  Adafruit_IO import  MQTTClient


AIO_USERNAME = "duchm"
AIO_KEY = "aio_XmoJ46ilGT41mT2ZlAbIx5DDQmQr"


client = MQTTClient(AIO_USERNAME , AIO_KEY)

client.connect()
client.loop_background()
time.sleep(5)

while True:
    value = random.randint(0, 100)
    client.publish("your_feed", value)
    time.sleep(30)
