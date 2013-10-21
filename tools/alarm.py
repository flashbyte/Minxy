#!/usr/bin/env python
from mpd import MPDClient
import time
maxVolume = 75
time_to_max_volume = 0.5  # TODO: Configure
mpd_host = '192.168.178.50'
mpd_port = 6600


client = MPDClient()
client.connect(mpd_host, mpd_port)
client.setvol(0)
client.playid(0)

# Push to maxVolume in time_to_max_volume
steps = 70 / (time_to_max_volume * 60)
counter = 0
while counter < maxVolume:
    client.setvol(int(counter))
    time.sleep(1)
    counter += steps

client.close()
