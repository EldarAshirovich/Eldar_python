import pydoc
from time import sleep, time
from datetime import datetime
import sys
"""
Autor Sabri Eldar

    1. Создать класс TrafficLight (светофор).
    определить у него один атрибут color (цвет) и метод running (запуск); атрибут реализовать как приватный;
    в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
    продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
    переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
    проверить работу примера, создав экземпляр и вызвав описанный метод.
    Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и завершать скрипт.
"""
class TrafficLight:
    _color = ['Красный', 'Жёлтый', 'Зелёный']
    
    def __init__(self):
        hold_time = time()
        self.hold_time = int('{:.0f}'.format(hold_time))
        self.timingmap = {self._color[0]: 3, self._color[1]: 2, self._color[2]: 4}
        self.color = self._color[0]
        self.tgl = 0
    
    def togle(self, color, n_time):
        h_time = self.hold_time
        if color == self._color[1] and n_time == h_time + self.timingmap[self._color[1]]:
            if self.tgl == 0:
                self.color = self._color[2]
            else:
                self.color = self._color[0]
            self.hold_time += self.timingmap[self._color[1]]
        elif color == self._color[0] and n_time == h_time + self.timingmap[self._color[0]]:
            self.color = self._color[1]
            self.hold_time += self.timingmap[self._color[0]]
            self.tgl = 0
        elif color == self._color[2] and n_time == h_time + self.timingmap[self._color[2]]:
            self.color = self._color[1]
            self.tgl = 1
            self.hold_time += self.timingmap[self._color[2]]
        return color
    
    def running(self):
        print('{:-^100}'.format('Светофор включен!'))
        i = 0
        while i<26:
            sleep(1)
            now = datetime.now()
            n_time = time()
            n_time = int('{:.0f}'.format(n_time))
            print(f'{now.strftime("%H-%M-%S")} -- {str(self.togle(self.color, n_time))}')
            # sys.stdout.write("\r{} ".format(f'{now.strftime("%H-%M-%S")} -- {str(self.togle(self.color, n_time))}'))
            # sys.stdout.flush()
            i+=1
        print('{:-^100}\n'.format('Светофор выключен!'))
    
    
run_trafficlight = TrafficLight().running()
