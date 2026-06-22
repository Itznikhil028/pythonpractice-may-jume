from sklearn.model_selection import train_test_split, cross_val_score
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression


study = [1,2,3,4,5,6,7,8,4,6,3,8]
marks = [25,38,52,65,72,85,89,93,96,68,82,91]

X = np.array(study).reshape(-1,1)
Y = np.array(marks)

X_train,X_test,y_train,y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

print(f'slope:    {model.coef_[0]:.2f}(marks increase per study hour)')
print(f'Intercept: {model.intercept_:.2f}(,arks at o hour study)')

y_pred = model.predict(X_test)
print(f'R score: {r2_score(y_test,y_pred)==0.5:.2f}')

new_pred = model.predict([[7]])[0]
print(f'student studying 7 hr predicted marks: {new_pred:.1f}')

plt.figure(figsize=(9,5))

plt.scatter(X,Y,color='blue',s=100,alpha=0.8,label='Actual')
plt.plot(X,model.predict(X),color='red',linewidth=2,label='Predicted score')
plt.xlabel('study hours/day'); 
plt.ylabel('exam marks')
plt.title('linear regression - study hours vs marks')
plt.legend()
plt.grid(True,alpha=0.3)
plt.show()