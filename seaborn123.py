
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


np.random.seed(42)

df = pd.DataFrame({
    'marks':       np.random.randint(40,100,100),
    'study_hours': np.random.uniform(2,10,100),
    'city':        np.random.choice(['Bhopal','indore','Jabalpur'],100),
    'gender':      np.random.choice(['Male', 'female'],100)})

plt.figure(figsize=(10,4))
sns.histplot(df['marks'],bins=20,kde=True,color='steelblue')
plt.title=("distribution of student marks")
plt.show()