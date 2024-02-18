import numpy as np
import matplotlib.pyplot as plt

# Choose number of chords to draw in the simulation:
num_chords = 10000


def draw_circle_and_triangle(ax):
    circle = plt.Circle((0, 0), 1, color='w', linewidth=2, fill=False)
    ax.add_patch(circle)  # Draw circle
    ax.plot([np.cos(np.pi / 2), np.cos(7 * np.pi / 6)],
            [np.sin(np.pi / 2), np.sin(7 * np.pi / 6)], linewidth=2, color='g')
    ax.plot([np.cos(np.pi / 2), np.cos(- np.pi / 6)],
            [np.sin(np.pi / 2), np.sin(- np.pi / 6)], linewidth=2, color='g')
    ax.plot([np.cos(- np.pi / 6), np.cos(7 * np.pi / 6)],
            [np.sin(- np.pi / 6), np.sin(7 * np.pi / 6)], linewidth=2, color='g')
    plt.show()


def bertrand_simulation1(method_number):
    # Simulation initialisation parameters
    count = 0

    # Figure initialisation
    plt.style.use('dark_background')  # use dark background
    ax = plt.gca()
    ax.cla()  # clear things for fresh plot
    ax.set_aspect('equal', 'box')
    ax.set_xlim((-1, 1))  # Set x axis limits
    ax.set_ylim((-1, 1))  # Set y axis limits

    # Repeat the following simulation num_chords times:
    for i in range(1,num_chords):
        theta1 = np.random.random()*2*np.pi
        theta2 = np.random.random()*2*np.pi
        x = np.cos([theta1, theta2])
        y = np.sin([theta1, theta2])
        length = np.sqrt(abs(x[0]-x[1]) * abs(x[0]-x[1]) + abs(y[0]-y[1]) * abs(y[0]-y[1]))
        count += (length > np.sqrt(3))
        print("Probability = {:.4f}".format(count / i))
        if i <= 1000:  # only plot the first 1000 chordsprint("Probability = {:.4f}".format(count / k))
            if length > np.sqrt(3):
                plt.plot(x, y, color='y', alpha=0.1)
            else:
                plt.plot(x, y, color='m', alpha=0.1)
    draw_circle_and_triangle(plt.gca())
    plt.show()

def bertrand_simulation2(method_number):
    # Simulation initialisation parameters
    count = 0

    # Figure initialisation
    plt.style.use('dark_background')  # use dark background
    ax = plt.gca()
    ax.cla()  # clear things for fresh plot
    ax.set_aspect('equal', 'box')
    ax.set_xlim((-1, 1))  # Set x axis limits
    ax.set_ylim((-1, 1))  # Set y axis limits

    # Repeat the following simulation num_chords times:
    for i in range(1,num_chords):
        theta1 = np.random.random()*2*np.pi
        radius = np.sqrt(np.random.random())
        x0 = np.cos(theta1) * radius
        y0 = np.sin(theta1) * radius
        m = (-1 * x0) / y0
        c = (x0 * x0 + y0 * y0) / y0
        A = m * m +1
        B = 2 * m * c
        C = c * c - 1
        x1 = (-B + np.sqrt(B * B - 4 * A * C)) /(2 * A)
        x2 = (-B - np.sqrt(B * B - 4 * A * C)) /(2 * A)
        y1 = m * x1 + c
        y2 = m * x2 + c
        length = np.sqrt(abs(x1-x2) * abs(x1-x2) + abs(y1-y2) * abs(y1-y2))
        count += (length > np.sqrt(3))
        print("Probability = {:.4f}".format(count / i))
        if i <= 1000:  # only plot the first 1000 chordsprint("Probability = {:.4f}".format(count / k))
            if length > np.sqrt(3):
                plt.plot([x1,x2],[y1,y2], color='y', alpha=0.1)
            else:
                plt.plot([x1,x2],[y1,y2], color='m', alpha=0.1)
    draw_circle_and_triangle(plt.gca())
    plt.show()



def bertrand_simulation3(method_number):
    # Simulation initialisation parameters
    count = 0

    # Figure initialisation
    plt.style.use('dark_background')  # use dark background
    ax = plt.gca()
    ax.cla()  # clear things for fresh plot
    ax.set_aspect('equal', 'box')
    ax.set_xlim((-1, 1))  # Set x axis limits
    ax.set_ylim((-1, 1))  # Set y axis limits

    # Repeat the following simulation num_chords times:
    for i in range(1, num_chords):
        theta1 = np.random.random() * 2 * np.pi
        radius = np.random.random()
        x0 = np.cos(theta1) * radius
        y0 = np.sin(theta1) * radius
        m = (-1 * x0) / y0
        c = (x0 * x0 + y0 * y0) / y0
        A = m * m + 1
        B = 2 * m * c
        C = c * c - 1
        x1 = (-B + np.sqrt(B * B - 4 * A * C)) / (2 * A)
        x2 = (-B - np.sqrt(B * B - 4 * A * C)) / (2 * A)
        y1 = m * x1 + c
        y2 = m * x2 + c
        length = np.sqrt(abs(x1 - x2) * abs(x1 - x2) + abs(y1 - y2) * abs(y1 - y2))
        count += (length > np.sqrt(3))
        print("Probability = {:.4f}".format(count / i))
        if i <= 1000:  # only plot the first 1000 chordsprint("Probability = {:.4f}".format(count / k))
            if length > np.sqrt(3):
                plt.plot([x1, x2], [y1, y2], color='y', alpha=0.1)
            else:
                plt.plot([x1, x2], [y1, y2], color='m', alpha=0.1)
    draw_circle_and_triangle(plt.gca())
    plt.show()


# method_choice = input('Choose method to simulate: ')
# bertrand_simulation1(1)
# bertrand_simulation2(1)
bertrand_simulation3(1)
