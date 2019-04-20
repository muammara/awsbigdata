
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTShadowClient
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
#import RPi.GPIO as GPIO
from sense_hat import SenseHat
import datetime,time
from datetime import date, datetime
from time import sleep
sense = SenseHat()



# A random programmatic shadow client ID.
SHADOW_CLIENT = "myShadowClient"

# The unique hostname that AWS IoT generated for 
# this device.
HOST_NAME = "avkun15yw21sh-ats.iot.us-east-1.amazonaws.com"

# The relative path to the correct root CA file for AWS IoT, 
# that you have already saved onto this device.
ROOT_CA = "root-CA.crt"

# The relative path to your private key file that 
# AWS IoT generated for this device, that you 
# have already saved onto this device.
PRIVATE_KEY = "rsp-home.private.key"

# The relative path to your certificate file that 
# AWS IoT generated for this device, that you 
# have already saved onto this device.
CERT_FILE = "rsp-home.cert.pem"

# A programmatic shadow handler name prefix.
SHADOW_HANDLER = "rsp-home"


 
# AWS IoT certificate based connection
myMQTTClient = AWSIoTMQTTClient("123afhlss456")
myMQTTClient.configureEndpoint(HOST_NAME, 8883)
myMQTTClient.configureCredentials(ROOT_CA, PRIVATE_KEY, CERT_FILE)
myMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec
 
#connect and publish
myMQTTClient.connect()
myMQTTClient.publish("rsp-home/info", "connected", 0)
 
#loop and publish sensor reading
while 1:
    t = round(sense.get_temperature(),2)
    p = sense.get_pressure()
    h = sense.get_humidity()
    now = datetime.utcnow()
    now_str = now.strftime('%Y-%m-%dT%H:%M:%SZ') #e.g. 2016-04-18T06:12:25.877Z
    instance = dht11.DHT11(pin = 4) #BCM GPIO04
    result = instance.read()
    if result.is_valid():
        payload = '{ "timestamp": "' + now_str + '","temperature": ' + str(t) + ',"humidity": '+ str(h) + ' }'
        print payload
        myMQTTClient.publish("rsp-home1/data", payload, 0)
        sleep(4)
    else:
        print (".")
        sleep(10)
