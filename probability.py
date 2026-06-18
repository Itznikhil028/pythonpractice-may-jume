import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from scipy.stats import norm


mean_h, std_h = 165, 7

prob = 1-norm.cdf(175, mean_h, std_h)
print(f'P(height > 175 cm) = {prob:.4f} = {prob*100:.2f}')
      
print(f'68 % od people: {mean_h-std_h:.0f}cm to {mean_h+std_h:.0f}cm')
print(f'95 % od people: {mean_h-2*std_h:.0f}cm to {mean_h+2*std_h:.0f}cm')
print(f'99.7 % od people: {mean_h-3*std_h:.0f}cm to {mean_h+3*std_h:.0f}cm')



