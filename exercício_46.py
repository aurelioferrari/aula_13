from time import sleep
from emoji import emojize

for c in range(10, 0, -1):
    print(c)
    sleep(1)
print(emojize("UHUL :boom: :boom: :boom:", use_aliases=True))
