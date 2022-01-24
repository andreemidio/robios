import logging
from threading import Thread

import paho.mqtt.client as mqtt
from django.apps import AppConfig


# from apps.producao.factory import savedata


class MqttClient(Thread):
    def __init__(self, broker, port, timeout, topics):
        super(MqttClient, self).__init__()

        self.client = mqtt.Client()
        self.broker = broker
        self.port = port
        self.timeout = timeout
        self.topics = topics
        self.total_messages = 0

    def on_message(self, client, userdata, msg):
        self.total_messages = self.total_messages + 1
        print(str(msg.payload) + "Total: {}".format(self.total_messages))
        # savedata(json.loads(msg.payload.decode()))

    def on_connect(self, client, userdata, flags, rc):
        client.subscribe(self.topics)

    def connect_to_broker(self):
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(self.broker, self.port, self.timeout)
        self.client.loop_forever()

    def run(self):
        self.connect_to_broker()


class ProducaoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.producao'

    def ready(self):
        logging.info('Sent From ready')
        MqttClient("localhost", 1883, 30, "hello/teste").start()

# https://stackoverflow.com/questions/68477402/listen-to-mqtt-topics-with-django-channels-and-celery
