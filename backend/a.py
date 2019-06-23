import requests
import time

# stream_url = 'http://audio12.broadcastify.com/twr7nd2qc15s4jy.mp3?nocache=9396187&xan=DCJP4HvtwMoXdH9HvtwMJ5vv342DfleDptcoX3dH9H48vtwMJ'
stream_url = 'http://audio13.broadcastify.com/cw8j1thymz32s5f.mp3?nocache=404062&xan=DCJP4HvtwMoXdH9HvtwMJ5vv342DfleDptcoX3dH9H48vtwMJ'

r = requests.get(stream_url, stream=True)


# with open('stream.mp3', 'wb') as f:
#   try:
#     for block in r.iter_content(1024):
#       f.write(block)
#       print('hi')
#   except KeyboardInterrupt:
#     pass

num = 0
seconds = time.time()
while(True):
  with open('audio/' + str(num) + '.mp3', 'wb') as f:
    try:
      for block in r.iter_content(1024):
        # print(str(num) + '.mp3 ' + str(time.time() - seconds) + 's')
        f.write(block)
        if (time.time() - seconds >= 60):
          num += 1
          seconds = time.time()
          print(str(num) + '.mp3 ')
          break
    except KeyboardInterrupt:
      pass