from Markov import Markov
from collections import Counter

city_weather = {
    'New York': 'rainy',
    'Chicago': 'snowy',
    'Seattle': 'rainy',
    'Boston': 'hailing',
    'Miami': 'windy',
    'Los Angeles': 'cloudy',
    'San Francisco': 'windy'
}


print("The number of occurrences of each weather condition over the 100 trials for each city")
print("----------------------------------")
predictions = {}
for city, weather in city_weather.items():
    weather_today = Markov(day_zero_weather=weather)
    weather_today.load_data(file_path='./weather.csv')
    ans = Counter(weather_today.get_weather_for_day(day=7, trials=100))
    predictions[city] = max(ans.items(), key=lambda x: x[1])[0]
    print("{}: {}".format(city, dict(ans)))

print()
print("Most likely weather in seven days")
print("----------------------------------")
for city, weather in predictions.items():
    print("{}: {}".format(city, weather))