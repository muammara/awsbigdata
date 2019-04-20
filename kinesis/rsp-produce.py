import boto3
import json
from datetime import datetime
import calendar
import random
import time
from sense_hat import SenseHat


my_stream_name = 'python-stream'

kinesis_client = boto3.client('kinesis', region_name='us-east-1')

def put_to_stream(thing_id, property_value, property_timestamp):
    """payload = {
                'prop': str(property_value),
                'timestamp': str(property_timestamp),
                'thing_id': thing_id
              }
    """
    payload =read_rsp()

    print (payload)

    put_response = kinesis_client.put_record(
                        StreamName=my_stream_name,
                        Data=json.dumps(payload),
                        PartitionKey=thing_id)
    #print(put_response)
def read_rsp(rspname='rsp-home')
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
    property_value = random.randint(40, 120)
    property_timestamp = calendar.timegm(datetime.utcnow().timetuple())
    thing_id = 'aa-bb'

    put_to_stream(thing_id, property_value, property_timestamp)

    # wait for 5 second
    time.sleep(5)
