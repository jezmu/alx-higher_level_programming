#!/usr/bin/python3
"""Test utilities"""
import os

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

def construct_path(file):
    return os.path.join(CURRENT_DIR, file)
