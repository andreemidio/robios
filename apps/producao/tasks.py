import logging

from celery import Task
from robios import api
from robios.config import RobiosConfig

from config.celery import app
from config.settings import ROBOT_ADDRESS, API_KEY, ROBOT_ID


def on_connect(mqttc, obj, flags, rc):
    print("rc: " + str(rc))


def on_message(mqttc, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))


def on_publish(mqttc, obj, mid):
    print("mid: " + str(mid))


def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))


def on_log(mqttc, obj, level, string):
    print(string)


# class TaskRobios(Task):
#
#     def __init__(self):
#         self.config = RobiosConfig(robot_address=ROBOT_ADDRESS, robot_id=ROBOT_ID)
#
#         self.robios = api.get(API_KEY, config=self.config)
#
#     def on_receive_message(context: str, data: str):
#         print(f'Receive message at context "{context}": {data}')

@app.task(bind=True)
def run(self, *args, **kwargs):
    # mqttc = mqtt.Client()
    # mqttc.on_message = on_message
    # mqttc.on_connect = on_connect
    # mqttc.on_publish = on_publish
    # mqttc.on_subscribe = on_subscribe
    #
    # mqttc.connect("localhost", 1883, 60)
    # mqttc.subscribe("hello/teste", 0)
    #
    # mqttc.loop_forever()
    # self.robios.add_message_callback('hello/teste', self.on_receive_message)
    # self.robios.ext().send_message('hello/teste', 'hello')
    #
    # self.robios.remove_message_callback('hello/teste', self.on_receive_message)
    #
    # self.robios.close()
    print("Hello World")
    logging.info("Hello World")
