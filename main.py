import numpy as np
from matplotlib import pyplot as plt
from numpy import sin,cos

n_start = 0 # Do you want to start the series from 1 or 0, change this to 0 for cosine.
pi = np.pi
n_terms = 10 # How many terms do you want to be plotted?
n_points = 1000 # This effects resolution of the graph. This value is fine.
start = -2*pi # Range to be plotted
stop = 2*pi

def cal_fourier(term_func):
    res = np.zeros(n_points)
    for i,x in enumerate(np.linspace(start,stop,n_points)):
        res[i] += np.sum([term_func(n,x) for n in range(n_start,n_terms)])
    return res

def cal_actual_func(actual_func):
    return [actual_func(x) for x in np.linspace(start,stop,n_points)]

# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    x = np.linspace(start,stop,n_points)
    # actual_func = lambda x:100*x-80
    # term_func = lambda n,x: ((200*sin(n*pi)-40*n*pi*cos(n*pi)-160*n*pi)/np.square(n*pi))*sin(n*pi*x)
    # actual_func = lambda x: 100
    # term_func = lambda n,x: (400/(n*pi))*sin(n*pi*x) if n%2==1 else 0
    # actual_func = lambda x:5*sin(4*pi*x)
    # term_func = lambda n,x: 5*(sin(12*pi-n*pi)/(12*pi-n*pi)-sin(12*pi+n*pi)/(12*pi+n*pi))*sin(n*pi*x)/3
    # actual_func = lambda x: 4*x/pi if 0<=x<=pi else 8-4*x/pi
    # def term_func(n,x):
    #     if n%2==0:
    #         return 0
    #     elif n%4==1:
    #         return 32*sin(n*x/2)/(n**2*pi**2)
    #     else:
    #         return -32*sin(n*x/2)/(n**2*pi**2)
    # actual_func = lambda x: 50*x*(1-x)
    # def term_func(n,x):
    #     if n==0:
    #         return 25/3
    #     elif n%2==0:
    #         return cos(n*pi*x)*-200/((n*pi)**2)
    #     else:
    #         return 0
    # actual_func = lambda x: x/2
    # term_func = lambda n,x: -sin(n*x)/n if n%2==0 else sin(n*x)/n
    # actual_func = lambda x: np.abs(x)
    # term_func = lambda n,x: 1 if n==0 else cos(n*pi*x/2)*(4*cos(n*pi)-4)/(n**2*pi**2)
    # actual_func = lambda x: np.abs(x)
    # term_func = lambda n,x: 0 if n==0 else sin(n*pi*x/2)*(-2*cos(n*pi)+2)/(n*pi)
    # actual_func = lambda x: 1
    # term_func = lambda n,x: sin(n*pi*x/2)*-2*(cos(n*pi)-1)/(n*pi)
    actual_func = lambda x: x**2
    term_func = lambda n,x: pi**2/3 if n==0 else cos(n*x)*4*cos(n*pi)/(n**2)

    actual = cal_actual_func(actual_func)
    series = cal_fourier(term_func)

    plt.plot(x,series,label='series')
    plt.plot(x, actual, label='actual')
    plt.legend()
    plt.show()