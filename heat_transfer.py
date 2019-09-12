"""
Heat Transfer Equations
"""

import numpy as np
from matplotlib import pyplot as plt


def solver(matl):
    """
 matl_tk, hs_T, hs_H, cs_T, cs_H
    :param matl:
    :param matl_tk:
    :param hs_T:
    :param hs_H:
    :param cs_T:
    :param cs_H:
    :return:
    """
    if matl[0] == "1":
        ans = "Aluminum"
    elif matl[0] == "2":
        ans = "Copper"
    else:
        ans = "Titanium"

    return ans


# george = ["1", 1, "mom"]
# print(solver(george))