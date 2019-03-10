import boto3
import json
from datetime import datetime
import calendar
import random
import time
from sense_hat import SenseHat 


my_stream_name = 'rsp'


kinesis_client = boto3.client('kinesis', region_name='us-east-1')

def put_to_stream(thing_id, temp,humidity,pressure, property_timestamp):
    payload = {
                'thing_id':str(thing_id),
                'temp': temp,
                'humidity':humidity,
                'pressure':pressure,
                'timedate':property_timestamp
                
                #'prop': str(property_value),
                #'timestamp': str(property_timestamp),
                #'thing_id': thing_id
              }
    print(payload)


    put_response = kinesis_client.put_record(
                        StreamName=my_stream_name,
                        Data=json.dumps(payload),
                        PartitionKey=thing_id)

while True:
    sense=SenseHat()
    temp=round(sense.get_temperature())
    humidity=round(sense.get_humidity())
    pressure=round(sense.get_pressure())
    property_timestamp = calendar.timegm(datetime.utcnow().timetuple())
    thing_id = 'rsp-home'
    put_to_stream(thing_id, temp,humidity,pressure, property_timestamp)

    # wait for 5 second
    time.sleep(600)