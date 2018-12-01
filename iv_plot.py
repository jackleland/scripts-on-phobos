import numpy as np
import matplotlib.pyplot as plt

e = 1.60e-19
k = 1.38e-23

def iv_characteristic_function(v, *parameters):
    I_0 = parameters[0]
    a = parameters[1]
    v_f = parameters[2]
    T_e = parameters[3]
    V = (v_f - v)/T_e
    return I_0 * (1 - np.exp(-e*V/k) + (a * np.float_power(np.absolute(V), 0.75)))


def simple_iv_characteristic_function(v, *parameters):
    I_0 = parameters[0]
    v_f = parameters[1]
    T_e = parameters[2]
    V = (v_f - v) / T_e
    return I_0 * (1 - np.exp(-e*V/k))


v_float = -20.5
e_temp = 6  # eV
I_0_sam = 32.774
a_sam = 0.0204

params = [I_0_sam, a_sam, v_float, e_temp]
params_simple = [I_0_sam, v_float, e_temp]


v = np.linspace(-10,10,100)
i_simple = simple_iv_characteristic_function(v, *params_simple)
i_sheath = iv_characteristic_function(v, *params)

plt.figure()
plt.plot(v, i_sheath, label='Sheath')
plt.plot(v, i_simple, label='Simple')
plt.legend()
plt.show()
