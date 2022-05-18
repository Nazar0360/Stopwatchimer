class Stopwatch(object):
    __stopwatches = {}
    __time = __import__('time')

    @staticmethod
    def get_stopwatches(wanted_name: str | None = None, name_index: int | None = None) -> \
            object | list[object] | dict | None:
        """
        If you want to get a stopwatch, you can get it by name,
        name_index, or both.

        :param wanted_name: str | None = None
        :type wanted_name: str | None
        :param name_index: int | None = None
        :type name_index: int | None
        :return: A list of stopwatches with the name wanted_name and name_index.
        """
        if wanted_name is None:
            if name_index is None:
                return Stopwatch.__stopwatches
            stopwatches_to_return = list()
            for name in Stopwatch.__stopwatches.keys():
                if int(name[1:name.find(']')]) == name_index:
                    stopwatches_to_return.append(Stopwatch.__stopwatches.get(name, "It shouldn't have been"))
            if len(stopwatches_to_return) == 0:
                stopwatches_to_return.append(None)
            if len(stopwatches_to_return) == 1:
                stopwatches_to_return = stopwatches_to_return[0]
            return stopwatches_to_return
        else:
            stopwatches_to_return = list()
            for name in Stopwatch.__stopwatches.keys():
                name: str
                if name[name.find(']') + 1:] == wanted_name:
                    stopwatches_to_return.append(Stopwatch.__stopwatches.get(name, "It shouldn't have been"))
            if len(stopwatches_to_return) > 1 and name_index is not None:
                obj_to_remove = list()
                for obj in stopwatches_to_return:
                    obj: Stopwatch
                    if obj.name_index != name_index:
                        obj_to_remove.append(obj)
                for obj in obj_to_remove:
                    stopwatches_to_return.remove(obj)
            if len(stopwatches_to_return) == 0:
                stopwatches_to_return.append(None)
            if len(stopwatches_to_return) == 1:
                stopwatches_to_return = stopwatches_to_return[0]
            return stopwatches_to_return

    def __init__(self, name: str = 'Stopwatch', round_time: int = None):
        self.__start: float = Stopwatch.__time.time()
        self.__pause: float | None = None
        self.__delay: float = 0
        self.__round: int = round_time
        self.__name: str = name
        self.__name_index: int = 0
        if name.lower() != 'secret':
            while f'[{self.__name_index}]' + name in Stopwatch.__stopwatches.keys():
                self.__name_index += 1
            Stopwatch.__stopwatches.update({f'[{self.__name_index}]' + self.__name: self})
        else:
            self.__name_index = -1

    def __str__(self) -> str:
        return f'[{self.name_index}]{self.name}(time={self.time}, start_t={self.start_time},' \
               f'pause_t={self.pause_time}, round={self.rounding}, __delay={self.__delay})'

    def pause_stopwatch(self) -> float | int:
        if not self.__pause:
            self.__pause = Stopwatch.__time.time()
        return self.time

    def resume_stopwatch(self):
        if self.__pause:
            self.__delay += Stopwatch.__time.time() - self.__pause
        self.__pause = None

    def start_stopwatch(self):
        self.__start = Stopwatch.__time.time()
        self.resume_stopwatch()
        self.__delay = 0

    @property
    def name(self) -> str:
        return self.__name

    @property
    def name_index(self) -> int:
        return self.__name_index

    @name.setter
    def name(self, name: str):
        Stopwatch.__stopwatches.pop(f'[{self.name_index}]' + self.name)
        self.__name_index = 0
        self.__name = name
        if name.lower() != 'secret':
            while f'[{self.__name_index}]' + name in Stopwatch.__stopwatches.keys():
                self.__name_index += 1
            Stopwatch.__stopwatches.update({f'[{self.__name_index}]' + self.__name: self})
        else:
            self.__name_index = -1

    @property
    def start_time(self) -> float:
        return self.__start

    @start_time.setter
    def start_time(self, start_time: float):
        self.__start = start_time

    @property
    def pause_time(self) -> float:
        return self.__pause

    @property
    def rounding(self) -> int:
        return self.__round

    @rounding.setter
    def rounding(self, rounding: int):
        self.__round = rounding

    @property
    def time(self) -> float:
        if self.__pause:
            if isinstance(self.__round, int):
                return round(self.__pause - self.__start - self.__delay, self.__round)
            return self.__pause - self.__start - self.__delay
        if isinstance(self.__round, int):
            return round(Stopwatch.__time.time() - self.__start - self.__delay, self.__round)
        return Stopwatch.__time.time() - self.__start - self.__delay

    @time.setter
    def time(self, stopwatch_time: float):
        self.__delay += self.time - stopwatch_time


class Timer(object):
    __timers = {}

    @staticmethod
    def get_timers(wanted_name: str | None = None, name_index: int | None = None) -> \
            object | list[object] | dict | None:
        """
        If you give it a name, it will return a list of all timers with that name. If you give it a name and an
        index, it will return a list of all timers with that name and index. If you give it an index, it will return
        a list of all timers with that index. If you give it nothing, it will return a dictionary of all timers

        :param wanted_name: str | None = None
        :type wanted_name: str | None
        :param name_index: The index of the timer
        :type name_index: int | None
        :return: A list of Timer objects.
        """
        if wanted_name is None:
            if name_index is None:
                return Timer.__timers
            timers_to_return = list()
            for name in Timer.__timers.keys():
                if int(name[1:name.find(']')]) == name_index:
                    timers_to_return.append(Timer.__timers.get(name, "It shouldn't have been"))
            if len(timers_to_return) == 0:
                timers_to_return.append(None)
            if len(timers_to_return) == 1:
                timers_to_return = timers_to_return[0]
            return timers_to_return
        else:
            timers_to_return = list()
            for name in Timer.__timers.keys():
                name: str
                if name[name.find(']') + 1:] == wanted_name:
                    timers_to_return.append(Timer.__timers.get(name, "It shouldn't have been"))
            if len(timers_to_return) > 1 and name_index is not None:
                obj_to_remove = list()
                for obj in timers_to_return:
                    obj: Timer
                    if obj.name_index != name_index:
                        obj_to_remove.append(obj)
                for obj in obj_to_remove:
                    timers_to_return.remove(obj)
            if len(timers_to_return) == 0:
                timers_to_return.append(None)
            if len(timers_to_return) == 1:
                timers_to_return = timers_to_return[0]
            return timers_to_return

    def __init__(self, timer_time: float, name: str = 'Timer'):
        self.__timer_time: float = timer_time
        self.__is_over: bool = False
        self.__stopwatch: Stopwatch = Stopwatch('secret')
        self.__stopwatch.pause_stopwatch()
        self.__name = name
        self.__name_index = 0
        if name.lower() != 'secret':
            while f'[{self.__name_index}]' + name in Timer.__timers.keys():
                self.__name_index += 1
            Timer.__timers.update({f'[{self.__name_index}]' + self.__name: self})
        else:
            self.__name_index = -1

    def __str__(self) -> str:
        return f'[{self.__name_index}]{self.__name}(timer_time={self.timer_time}, is_over={self.is_over},' \
               f'rest_time={self.rest_time})'

    def start_timer(self):
        self.__stopwatch.start_stopwatch()

    def pause_timer(self) -> float:
        self.__stopwatch.pause_stopwatch()
        return self.rest_time

    def resume_timer(self):
        self.__stopwatch.resume_stopwatch()

    @property
    def name(self) -> str:
        return self.__name

    @property
    def name_index(self) -> int:
        return self.__name_index

    @name.setter
    def name(self, name: str):
        Timer.__timers.pop(f'[{self.name_index}]' + self.name)
        self.__name_index = 0
        self.__name = name
        if name.lower() != 'secret':
            while f'[{self.__name_index}]' + name in Timer.__timers.keys():
                self.__name_index += 1
            Timer.__timers.update({f'[{self.__name_index}]' + self.__name: self})
        else:
            self.__name_index = -1

    @property
    def rest_time(self) -> float:
        return max(self.__timer_time - self.__stopwatch.time, 0)

    @property
    def timer_time(self) -> float:
        return self.__timer_time

    @timer_time.setter
    def timer_time(self, timer_time: float):
        self.__timer_time = timer_time

    def modify_timer_time(self, difference: float):
        """
        It adds the difference to the timer time

        :param difference: The amount of time to add to the timer
        :type difference: float
        """
        self.__timer_time += difference

    @property
    def is_over(self) -> bool:
        if self.rest_time == 0:
            self.__is_over = True
        else:
            self.__is_over = False
        return self.__is_over


if __name__ == '__main__':
    # Running the tests for the stopwatch and timer.
    from test_stopwatchimer import *

    test_stopwatch()
    test_timer()
