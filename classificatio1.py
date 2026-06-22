
from sklearn.model_selection import train_test_split, cross_val_score
import numpy as np
from scipy import stats
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import seaborn as sns; import matplotlib.pyplot as plt 

# np.random.seed(42); n=300
# study = np.random.uniform(1,10,n)
# attend = np.random.uniform(40,100,n)
# tasks = np.random.randint(0,11,n)

# score = study*5 + attend>0.3 + tasks*2 + np.random.normal(0,8,n)
# passed=(score > 65).astype(int)
# df = pd.DataFrame({'study': study, 'attend':attend,'tasks':tasks, 'passed':passed})
# X=df[['study','attend','tasks']]
# y=df['passwd']

# X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

# scaler = StandardScaler()
# Xtr = scaler.fit_transform(X_train)
# Xte = scaler.transform(X_test)
# model=LogisticRegression()
# model.fit(Xtr,y_train)
# y_pred = model.predict(Xtr)
# print(f'accuracy: {accuracy_score(y_test,y_pred):.1f}%')
# print(classification_report(y_test,y_pred,target_names=['fail','pass']))

# cm = confusion_matrix(y_test,y_pred)
# sns.heatmap(cm,annot=True,fmt='d',cmap='blues',xticklabels=['fail','pass'],yticklabels=['fail','pass'])
# plt.title('confusion matrix'); plt.show()

# new = scaler.transform(([7,85,9]))
# pred = model.predict(new)[0]
# prob = model.predict_proba(new)[0]
# print(f'prediction: {"PASS" if pred ==1 else "FAIL"} | Probability: {prob[1]*100:.1f}%')
from sklearn .tree import DecisionTreeClassifier, export_text, plot_tree
from sklearn.datasets import load_iris
iris = load_iris()
X,y = iris.data, iris.target
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)


dt = DecisionTreeClassifier(max_depth=3,random_state=42)
dt.fit(X_train,y_train)
print(f'Decision tree accuracy: {accuracy_score(y_test,dt.predict(X_test))*100:.1f}')
print(export_text(dt,feature_names=list(iris.feature_names)))

plt.figure(figsize=(14,6))
plot_tree(dt,feature_names=iris.feature_names,class_names=iris.target_names,filled=True,rounded=True, fontsize=9)
plt.title('Decision tree, iris clasification'); plt.show()

rf = RandomForestClassifier(n_estimators=100,random_state=42)

rf.fit(X_train,y_train)
print(f'Random forest accuracy: {accuracy_score(y_test,rf.predict(X_test))*100:.1f}')


imp = pd.Series(rf.feature_importances_,index=iris.feature_names).sort_values(ascending=False)
imp.plot(kind='bar',color='blue')
plt.title('feature Importance'); plt.tight_layout();plt.show()