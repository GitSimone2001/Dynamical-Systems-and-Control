import numpy as np
import matplotlib.pyplot as plt

''' 
Discrete-Time Simulation of a single-variable dynamical system 
with constant input, using Euler Approximation 
'''

# Sampling period, Total period, Total samples
Tsample = 0.1
Ttot = 30
N = int(Ttot/Tsample)


def simulate_sys_response(a, b, xk, u):
    # Data init
    data = [xk]

    # Simulate (with Euler Approximation)
    for k in range(N):
        xk_1 = (1 - a * Tsample) * xk + Tsample * b * u
        xk = xk_1
        data.append(xk_1)

    # Plot Results
    t = np.arange(0, Ttot + Tsample, Tsample)
    plt.plot(t, data)

    # Plot Format
    plt.title('dx/dt = -ax(t) + bu')
    plt.xlabel('t[s]')
    plt.ylabel('x(t)')
    plt.grid()
    plt.axis([0, 30, -5, 10])
    plt.show()


simulate_sys_response(1, 1, -3, 9)

# Expect results of the form x(t) = exp(-at)x0 - (bu/a)*exp(-at) + (bu/a)
# x(steady state) = bu/a

