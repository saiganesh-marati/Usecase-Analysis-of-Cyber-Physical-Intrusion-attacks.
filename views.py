from django.shortcuts import render, redirect
from django.http import HttpResponse
import pickle
import math as m
import numpy as np
import pandas as pd
import seaborn as sns
import io
import urllib, base64
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, recall_score, f1_score, precision_score, confusion_matrix


def index(request):
    return render(request,'index.html')

def idor_page(request):
    return render(request,'idor_page.html')

def Sqli_page(request):
    return render(request,'Sqli_page.html')


def Otpbp_page(request):
    return render(request,'Otpbp_page.html')


def xss_page(request):
    return render(request,'xss_page.html')

def Htmli_page(request):
    return render(request,'Htmli_page.html')

def ssrf_page(request):
    return render(request,'ssrf_page.html')

def hhi_page(request):
    return render(request,'hhi_page.html')
def pt_page(request):
    return render(request,'pt_page.html')







