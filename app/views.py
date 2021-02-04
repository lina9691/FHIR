#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 15:17:33 2021

@author: fisher
"""

from app import app
from flask import Flask, render_template,request
import json


@app.route("/",methods = ['GET'])
def index():
    title = {'title':'Patient'}
    Nom = request.args.get(("Nom"))
    Prenom = request.args.get('Prenom')
    user = {'Nom':str(Nom),'Prenom': str(Prenom)}
    return render_template ('index.html',title=title, user=user)

