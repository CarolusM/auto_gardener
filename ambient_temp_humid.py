

import plotly
import pandas as pd
import numpy as np
import datetime
#import Adafruit_DHT

# Set sensor type : Options are DHT11,DHT22 or AM2302
# sensor = Adafruit_DHT.DHT11

# Set GPIO sensor is connected to
gpio = 17


columns = ['date', 'amb_temp', 'amb_humid']
pd_SensTrack = pd.DataFrame(columns=columns)
pd_SensTrack.append({'date':'bla', 'amb_temp':20, 'amb_humid':50})
pd_SensTrack.append({'date':'bla', 'amb_temp':21, 'amb_humid':45})
pd_SensTrack.append({'date':'bla', 'amb_temp':22, 'amb_humid':40})

print(pd_SensTrack)

# humidity_record = []
# temperature_record = []
#
# # Reading the DHT11 is very sensitive to timings and occasionally
# # the Pi might fail to get a valid reading. So check if readings are valid.
# while True:
#
#   # Use read_retry method. This will retry up to 15 times to
#   # get a sensor reading (waiting 2 seconds between each retry).
#   #humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
#   humidity, temperature = [50, 20]
#   if humidity is not None and temperature is not None:
#     print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
#     humidity_record.append(humidity)
#     temperature_record.append(temperature)
#   else:
#     print('Failed to get reading. Try again!')
#     pass



