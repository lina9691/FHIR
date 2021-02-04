#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 15:15:46 2021

@author: fisher
"""

from flask import Flask
app= Flask(__name__)
from app import views
