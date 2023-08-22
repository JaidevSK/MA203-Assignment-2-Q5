# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 18:25:05 2023
@author: jaidev
"""

import streamlit as st
st.write("# von Karman Equation Application")
st.write(" MA 203 Numerical Methods Assignment 2 Problem 5")
st.write(" Made By: Jaidev S. K.")

import math
import numpy as np
import matplotlib.pyplot as plt


Re = st.slider('#### Select the value of Re', 2500, 1000000, 15000)

def f(f):
    return 1 / math.sqrt(f) - 4 * math.log10(Re * math.sqrt(f)) + 0.4

def g(f):
    return 1/(4*math.log10(Re*math.sqrt(f))-0.4)**2

def fixed_point_iteration(g, x0, tolerance):
    x = x0
    while True:
        x_next = g(x)
        if abs(x_next - x)/x_next < tolerance:
            break
        x = x_next
    return x


initial_guess = 1
tolerance = 1e-8

fixed_point = fixed_point_iteration(g, initial_guess, tolerance)
st.write(f"#### The value of f is : {fixed_point}")


x = np.arange(0.001,0.01,0.0001)
y = []
for i in x:
    y.append(f(i))
y=np.array(y)
fig = plt.figure()
plt.plot(x,y)
plt.xlabel("Value of f")
plt.ylabel("Value of f(f)")
plt.title("Plot of f vs f(f) for verification")
plt.grid()
st.pyplot(fig)

# import plotly.express as px
# import pandas as pd
# df = pd.DataFrame(dict(
#     x = x,
#     y = y))
# fig = px.line(df, x="Value of f", y="Value of f(f)", title="Plot of f vs f(f) for verification") 
# st.plotly_chart(fig)

st.write("I have used the fixed point iteration method")
st.write("It is an open numerical method to find the approximate root of the equation. I have set the threshold of approximate error as 10^-8 and the value of Re is taken as input. The output is the value of f, that is the 'Fanning friction f' and a plot corresponding to the value of fn(f) and f. The expression of fn(f) is:  1/math.sqrt(f) - 4\*math.log10(Re*math.sqrt(f)) + 0.4")
st.write("## Made By: Jaidev S. K. 103")
