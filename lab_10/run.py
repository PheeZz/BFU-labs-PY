import matplotlib.pyplot as plt
from matplotlib import animation
import scipy as sp
import numpy as np


def legendre_polynomial(x, n):
    # realization of legendre polynomial by Scipy
    return sp.special.eval_legendre(n, x)


def poly_from_one_to_eight(x):
    # create list of y values for each polynomial
    y = [legendre_polynomial(x, i) for i in range(8)]
    # create list of colors for each polynomial
    colors = ['red', 'green', 'blue', 'yellow',
              'black', 'purple', 'orange', 'brown']
    # create list of labels for each polynomial
    labels = ['1', 'x', 'x^2', 'x^3', 'x^4', 'x^5', 'x^6', 'x^7']
    # create figure
    fig = plt.figure()
    # create axes
    ax = fig.add_subplot(111)
    # create legend
    legend = ax.legend(loc='upper right')
    # create plot for each polynomial
    for i in range(8):
        ax.plot(x, y[i], color=colors[i], label=labels[i])
    plt.legend()
    plt.title("Полиномы Лежандра")
    plt.show()


def show_legendre():
    # create list of x values
    x = sp.linspace(-1, 1, 100)
    # create plot
    poly_from_one_to_eight(x)


# def lissajous_figure(x):
#     # 4 graphs with different parameters of frequency (3:2), (3:4), (5:4), (5:6)
#     # create figure
#     fig = plt.figure()
#     # create axes
#     ax = fig.add_subplot(111)
#     # create legend
#     # create plot for each graph
#     ax.plot(np.sin(3 * sp.pi * x), np.sin(2 * sp.pi * x),
#             color='red', label='3:2')
#     ax.plot(np.sin(3 * sp.pi * x), np.sin(4 * sp.pi * x),
#             color='green', label='3:4')
#     ax.plot(np.sin(5 * sp.pi * x), np.sin(4 * sp.pi * x),
#             color='blue', label='5:4')
#     ax.plot(np.sin(5 * sp.pi * x), np.sin(6 * sp.pi * x),
#             color='yellow', label='5:6')
#     plt.legend()
#     plt.title("Фигура Лиссажу")
#     plt.show()


# def show_lissajous():
#     # create list of x values
#     x = sp.linspace(0, 1, 100)
#     # create plot
#     lissajous_figure(x)


def lissajous_figure_animated(i):
    """
    Реализовать с помощью Matplotlib анимацию врашения фигуры Лисажу
    при нулевом сдвиге фаз и изменении соотношения частот от 0 до 1
    animate one line by changing the data of the line
    """
    ax = plt.axes(xlim=(-1, 1), ylim=(-1, 1))
    line, = ax.plot([], [], lw=2)
    line.set_data(np.array([np.sin(i*t) for t in np.linspace(-5 * np.pi, 5 * np.pi, 100)]),
                  np.array([np.sin(t) for t in np.linspace(-5 * np.pi, 5 * np.pi, 100)]))
    return line,


def lissajous_animated():
    anim = animation.FuncAnimation(
        plt.figure(), lissajous_figure_animated, frames=np.linspace(0.0001, 1, num=100), interval=20, blit=False)

    anim.save('lissajous.gif', writer='imagemagick', fps=30)

    plt.show()


if __name__ == '__main__':
    # show_legendre()
    # show_lissajous()
    lissajous_animated()
