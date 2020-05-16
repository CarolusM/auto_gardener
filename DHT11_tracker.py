

import pandas as pd
import numpy as np
import datetime
import time
import warnings
import os
#import Adafruit_DHT

# Set sensor type : Options are DHT11,DHT22 or AM2302
# sensor = Adafruit_DHT.DHT11

# Set GPIO sensor is connected to
gpio = 17


class DHT11:

  def __init__(self, gpio):
    self.gpio = gpio
    #self.sensor = Adafruit_DHT.DHT11
    self.last_temperature = None
    self.last_humidity = None
    self.last_date = None


  def update_readings(self):

    [humid, temp] = self.read()

    if humid is not None and temp is not None:
      self.last_temperature = temp
      self.last_humidity = humid
      self.last_date = datetime.datetime.now()
      return 1
    else:
      return 0

  def read(self):

    # humid, temp = Adafruit_DHT.read_retry(self.sensor, self.gpio)
    # return [humidity, temperature]
    return [50.0, 22.4]

  def get_last_reading(self):

    return [self.last_date, self.last_temperature, self.last_humidity]


  def append_to_file(self, file_path):

    assert os.path.isfile(file_path), "File does not exist. Create it first"
    with open(file_path, 'a') as f:
      f.write("{} {} {}\n".format(self.last_date, self.last_temperature , self.last_humidity))

  def create_file(self, file_path):

    if not os.path.isfile(file_path):
      with open(file_path, 'w') as f:
        f.write("{}\n".format("date time temperature humidity"))
    else:
      warnings.warn("File already exists... passing")
      pass



if __name__ == '__main__':

  DHT11_sensor = DHT11(17)

  hist_path = './history.txt'
  DHT11_sensor.create_file(hist_path)

  time.sleep(60-datetime.datetime.now().minute)
  #for i in range(3):
  while True:

    while not DHT11_sensor.update_readings():
      warnings.warn("Warning.......Some error ocurred while reading, retrying in 2 secs")
      time.sleep(2)

    DHT11_sensor.append_to_file(hist_path)
    
    print(DHT11_sensor.get_last_reading())

    time.sleep(60)

    
