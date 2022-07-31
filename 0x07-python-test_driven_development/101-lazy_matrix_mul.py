#!/usr/bin/python3
"""matrix multiplication using numpy"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """matrix multiplication: two list are taken as arguments"""
    return (np.matmul(m_a, m_b))
