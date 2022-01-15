import time

class TrafficLight:

    def running(self):
        while True:
            self.__color = '|Красный|'
            print(f'{self.__color}')
            time.sleep(7)
            self.__color = '|Желтый |'
            print(f'{self.__color}')
            time.sleep(2)
            self.__color = '|Зеленый|'
            print(f'{self.__color}')
            time.sleep(8)
            break

traffic_light = TrafficLight()
traffic_light.running()