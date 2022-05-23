#!/usr/bin/python3
"""Lazy matrix multiplication using numpy library"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Function that multiplies 2 matrices
    Arguments:
        m_a ([[]]): first matrix
        m_b ([[]]): second matrix
    """
    return(np.matmul(m_a, m_b))
