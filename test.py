import random

from auto_adb import auto_adb

# adb = auto_adb()
# cmd = 'shell input roll {x1} {y1}'.format(
#     x1=624,
#     y1=423,
# )
# adb.run(cmd)
for i in range(10):
    print(random.randint(-4,4))