
# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd
# import seaborn as sns


# np.random.seed(42)

# df = pd.DataFrame({
#     'marks':       np.random.randint(40,100,100),
#     'study_hours': np.random.uniform(2,10,100),
#     'city':        np.random.choice(['Bhopal','indore','Jabalpur'],100),
#     'gender':      np.random.choice(['Male', 'female'],100)})

# plt.figure(figsize=(10,4))
# sns.histplot(df['marks'],bins=20,kde=True,color='steelblue')
# plt.title=("distribution of student marks")
# plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


salaries=[22,28,35,42,38,55,48,60,72,85,30,45,52,65,28,34,41,58,75,90]

#central tendency
mean=np.mean(salaries)
median=np.median(salaries)
mode=stats.mode(salaries,keepdims=True).mode[0]

print(f'mean Rs {mean:1f}K')
print(f'median Rs {median}K')
print(f'mode Rs {mode}K')

std=np.std(salaries)
var=np.var(salaries)
rng=max(salaries)-min(salaries)
q1=np.percentile(salaries,25)
q3=np.percentile(salaries,75)
iqr=q3-q1

print(f'std deviation : {std:.2f}K (most important spread measure)')
print(f'IQR : {iqr}K (q1={q1},q3={q3})')

lower=q1-1.5*iqr
upper=q3+1.5*iqr
outliers=[x for x in salaries if x < lower or x > upper]
print(f'outliers: {outliers}')
print(lower)
print(upper)


np.random.seed(42)
study = np.random.uniform(2, 10, 60)
marks = study * 8 + np.random.normal(0, 10, 60)
marks = np.clip(marks, 30, 100)
absemt = 10 - study + np.random.normal(0, 1, 60)

df = pd.DataFrame({'study_hours':study,'marks':marks, 'absensces':absemt})

corr_matrix = df.corr()
print(corr_matrix.round(3))

plt.figure(figsize=(6,4))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=+1, fmt='.2f')
plt.title('correlation matrix'); plt.show()


r, p_value = stats.pearsonr(study, marks)
print(f'study-marks correlation: r=(r/:.3f), p=(p_value.4f)')
print('interpretation','strong positive' if r>0.7 else 'Moderate' if r>0.4 else 'weak')