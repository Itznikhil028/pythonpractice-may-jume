from sklearn.model_selection import train_test_split, cross_val_score

import numpy as np

# np.random.seed(42)
# X = np.random.randn(500, 5)
# y = np.random.randint(0,2,500)

# X_train,X_test,y_train,y_test = train_test_split(
#     X,y ,test_size=0.2, random_state=42, stratify=y

# )
# print(f'Training sampl: {len(X_train)} | Test Samples: {len(X_test)}')

# from sklearn.ensemble import RandomForestClassifier
# model = RandomForestClassifier(n_estimators=50, random_state=42)
# cv_scores = cross_val_score(model, X, y, cv=5, scoring='accuracy' )
# print(f'CV Scores each fold:{cv_scores.round(3)}')
# print(f'Mean: {cv_scores.mean():.4f}+-{cv_scores.std():.4f}')

from scipy import stats
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression


n_A, conv_A = 1000, 52 
n_b, conv_b = 1000,68
rate_A =  conv_A / n_A
rate_b = conv_A /n_b

print(f'version A conversion reate {rate_A*100:.1f}%')
print(f'version b conversion reate {rate_b*100:.1f}%')
print(f'Improvment{(rate_b-rate_A)/rate_A*100:.1f}%')


table = [[conv_A, n_A-conv_A],[conv_b, n_b-conv_b]]
chi2, p_value, dof, ecpected = stats.chi2_contingency(table)

print(f'chi-square:{chi2:.4f}')
print(f'P-value: {p_value:.4f}')
print('result:','SIGNIFICANT - B is better!' if p_value<0.05 else 'NOT SIGNIFICANT- COULD BE RANDOM')



