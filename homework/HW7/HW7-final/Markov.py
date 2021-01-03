import numpy as np


class Markov:
    def __init__(self, day_zero_weather=None): # You will need to modify this header line later in Part C
        self.data = np.array([])
        self.d = {'sunny': 0, 'cloudy': 1, 'rainy': 2, 'snowy': 3, 'windy': 4, 'hailing': 5}
        self.day_zero_weather = day_zero_weather
        self._current_day = 0
        self._current_day_weather = day_zero_weather

    def load_data(self, file_path='./weather.csv'):
        self.data = np.genfromtxt(file_path, delimiter=',')

    def get_prob(self, current_day_weather, next_day_weather):
        if current_day_weather not in self.d:
            raise Exception("Current day not specified!")
        if next_day_weather not in self.d:
            raise Exception("Next day not specified!")

        return self.data[self.d[current_day_weather], self.d[next_day_weather]]

    def __iter__(self):
        return MarkovIterator(self, self.day_zero_weather)

    def _reset(self):
        self._current_day_weather = self.day_zero_weather
        self._current_day = 0

    def _simulate_weather_for_day(self, day):
        if day < 0:
            raise Exception("Day should not be less than 0!")
        self._reset()
        if day == 0:
            return self._current_day_weather
        for _ in range(day):
            new_weather = next(iter(self))
        return new_weather

    def get_weather_for_day(self, day, trials=100):
        if trials <= 0 or day < 0:
            raise Exception("Day and trials should be non-negative!")
        ans = []
        for i in range(trials):
            ans.append(self._simulate_weather_for_day(day))
        return ans


class MarkovIterator:
    def __init__(self, mk: Markov, day_zero_weather):
        self.mk = mk
        self.curr = day_zero_weather

    def __iter__(self):
        return self

    def __next__(self):
        next_day_prob = [self.mk.get_prob(self.curr, i) for i in self.mk.d.keys()]
        self.curr = np.random.choice(a=list(self.mk.d.keys()), p=next_day_prob)
        return self.curr
