import time
import sys


class TrafficLight:
    def __init__(self):
        self.__color = ''

    def running(self):
        schedule = {
            "Красный": 7,
            "Желтый": 2,
            "Зеленый": 9
        }
        for key in schedule:
            self.__color = key
            for i in range(schedule[key], 0, -1):
                string = (key + '    ')[:10] + str(i) + '\r'
                sys.stdout.write(string)
                time.sleep(1)
        self.__color = ''


a = TrafficLight()
a.running()
