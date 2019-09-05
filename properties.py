"""
Material Properties
"""

import numpy as np


def conductivity(material, temperature):
    """
    conductivity
    :param material:
        Name of Material
    :param temperature:
        Temperature of Material in [F]
    :return:
        Conductivity of Material at Given Temperature in [Btu/(hr*ft*F)]
    """

    if material.upper() == "AIR":
        T = [-300, -200, -100, -50, -20, 0, 10, 20, 30, 40,
                 50, 60, 70, 80, 100, 120, 140, 160, 180, 200,
                 250, 300, 350, 400, 450, 500, 600, 700, 800, 1000,
                 1200, 1400, 1600, 1800, 2000]
        k = [0.00484, 0.00788, 0.01068, 0.012, 0.01277, 0.01328, 0.01353, 0.01378, 0.01402, 0.01427,
                 0.01451, 0.01476, 0.015, 0.01524, 0.01571, 0.01618, 0.01664, 0.0171, 0.01755, 0.018,
                 0.01911, 0.02018, 0.02123, 0.02226, 0.02327, 0.02426, 0.0262, 0.02807, 0.0299, 0.03342,
                 0.0368, 0.04007, 0.04325, 0.04635, 0.04941]
    elif material.upper() == "ALUMINUM":
        T = [-100, 100]
        k = [10, 10]
    elif material.upper() == "COPPER":
        T = [-100, 100]
        k = [10, 10]
    elif material.upper() == "TITANIUM":
        T = [-100, 100]
        k = [10, 10]
    else:
        T = [-1, 1]
        k = [1, 1]

    cond = np.interp(temperature, T, k)

    return cond

print(conductivity('air',1000))
