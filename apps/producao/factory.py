# import django
#
# from apps.producao.models import ParadasProducao
#
# django.setup()
#
#
# def savedata(data):
#     print(f"{data['data']}\n\n\n")
#
#     parada = ParadasProducao.objects.create(messaging=data['data'])
#
#     return parada.id

# import paho.mqtt.client as mqtt
#
# broker_url = "mqtt.eclipse.org"
# broker_port = 1883
#
#
# def on_connect(client, userdata, flags, rc):
#     print("Connected With Result Code "(rc))
#
#
# def on_message_from_kitchen(client, userdata, message):
#     print("Message Recieved from Kitchen: " + message.payload.decode())
#
#
# def on_message_from_bedroom(client, userdata, message):
#     print("Message Recieved from Bedroom: " + message.payload.decode())
#
#
# def on_message(client, userdata, message):
#     print("Message Recieved from Others: " + message.payload.decode())
#
#
# client = mqtt.Client()
# client.on_connect = on_connect
# # To Process Every Other Message
# client.on_message = on_message
# client.connect(broker_url, broker_port)
# client.subscribe("TestingTopic", qos=1)
# client.subscribe("KitchenTopic", qos=1)
# client.subscribe("BedroomTopic", qos=1)
# client.message_callback_add("KitchenTopic", on_message_from_kitchen)
# client.message_callback_add("BedroomTopic", on_message_from_bedroom)
# client.loop_forever()
