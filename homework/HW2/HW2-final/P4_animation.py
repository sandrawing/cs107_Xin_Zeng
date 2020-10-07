import numpy
import matplotlib.pyplot as plt
import datetime
import math


def get_coordinate(length_of_hand):
    def inner(theta_of_hand):
        radian = theta_of_hand / 180 * math.pi
        x = length_of_hand * numpy.cos(radian)
        y = length_of_hand * numpy.sin(radian)
        return (x, y)
    return inner


num_plot = 0
max_plot = 100
# plot the number of max_plot plots
fig = plt.figure(figsize=(6, 6))
fig.show()
while num_plot < max_plot:
    num_plot += 1
    ### Closure defined up here
    currentDT = datetime.datetime.now()
    hour = currentDT.hour
    minute = currentDT.minute
    second = currentDT.second

    # Calculate theta in degrees for each hand
    theta_hour = 90 - 30 * hour - minute / 2
    theta_minute = 90 - 6 * minute
    theta_second = 90 - 6 * second

    # Specify the length of hour, minute and second hands
    length_hour = 1
    length_minute = 2
    length_second = 3

    # hour_hand = name_of_closure(length_of_hour_hand)
    hour_hand = get_coordinate(length_hour)
    # x_hour, y_hour = hour_hand(theta_hour)
    x_hour, y_hour = hour_hand(theta_hour)

    minute_hand = get_coordinate(length_minute)
    x_minute, y_minute = minute_hand(theta_minute)

    second_hand = get_coordinate(length_second)
    x_second, y_second = second_hand(theta_second)

    # Plot the clock
    fig.canvas.draw()
    plt.cla()
    plt.plot([0, x_hour], [0, y_hour], linewidth=5)
    plt.plot([0, x_minute], [0, y_minute], linewidth=4)
    plt.plot([0, x_second], [0, y_second], linewidth=2)
    plt.axis([-3, 3, -3, 3])
    plt.pause(0.1)

