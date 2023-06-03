from scheduler import *                                                                                                                                      
import time                                                                                                                                                  
from task1 import Task1                                                                                                                                      
from task2 import Task2                                                                                                                                      
from datetime import datetime         
#pip install adafruit-io
import random
import  sys
from  Adafruit_IO import  MQTTClient

AIO_USERNAME = "duchm"
AIO_KEY = "aio_XmoJ46ilGT41mT2ZlAbIx5DDQmQr"                

client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.connect()
client.loop_background()
time.sleep(5)

current_time = datetime.now().time()                                                                                                                         
hour = current_time.strftime("%H")                                                                                                                           
minute = current_time.strftime("%M")                                                                                                                         
                                                                                                                                                             
scheduler = Scheduler()                                                                                                                                      
task1 = Task1()                                                                                                                                              
task2 = Task2()                                                                                                                                              
                                                                                                                                                             
scheduler.SCH_Add_Task(task1.Task1_Run, 1000,5000) # 1s sau chạy và 5s chạy 1 lần                                                                            
scheduler.SCH_Add_Task(task2.Task2_Run, 3000,5000) # nếu task thực hiện 1 lần thì 5000 để thành 0                                                            
                                                                                                                                                             
# print("Hour:", hour)                                                                                                                                       
# print("Minute:", minute)                                                                                                                                   
                                                                                                                                                             
while True:                                                                                                                                                  
    scheduler.SCH_Update()                                                                                                                                   
    scheduler.SCH_Dispatch_Tasks()                                                                                                                           
    time.sleep(0.1)   
    value = random.randint(0, 100)
    client.publish("your_feed", value)
    time.sleep(30)