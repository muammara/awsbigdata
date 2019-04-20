import boto3
import json
from datetime import datetime
import calendar
import random
import time
from sense_hat import SenseHat

my_stream_name = ''
rsp_id= 'rsp-home'
kinesis_client = boto3.client('kinesis', region_name='us-east-1')

def put_to_stream(payload):
    put_response = kinesis_client.put_record(
                            StreamName=my_stream_name,
                            Data=json.dumps(payload),
                            PartitionKey=rsp_id)

def read_rsp(rspname="rsp-home"):
    sense = SenseHat()
    sense.clear()
    # Take readings from all three sensors
    t = sense.get_temperature()
    p = sense.get_pressure()
    h = sense.get_humidity()
    # Round the values to one decimal place
    t = round(t, 1)
    p = round(p, 1)
    h = round(h, 1)
    rspenv= {
            'temp':t,
            'pressure':p,
            'humidity':h,
            'thing':rspname
    }
    return(rspenv)


while True:
    payload =read_rsp(rsp_id)
    print (payload)
    put_to_stream(payload)
    # wait for 5 second
    time.sleep(5)
