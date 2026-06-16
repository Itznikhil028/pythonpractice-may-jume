import matplotlib.pyplot as plt

# months = ['Jab','feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
# sales = [45,55,66,79,86,64,73,96,87,77,84,98]

# plt.figure(figsize=(12,5))

# plt.plot( months, sales, marker='o',color='lightgreen', linewidth=2, markersize=8)
# plt.fill_between(months,sales, alpha=0.15, color='yellow')
# plt.title('Monthly sales 2024 (Rs. thousands)', fontsize=14, fontweight='bold')
# plt.xlabel('months')
# plt.ylabel('sales (RS. k)')
# plt.grid(True, alpha=0.3)
# plt.tight_layout()
# plt.show()


# Teams = ['Mumbai','chennai','rcb','kolkata','hydrabad']
# Tropies = [5,5,2,3,1]
# colors = ['#2196f3',"#eded04","#e90707","#370256","#f48600"]

# plt.figure(figsize=(9,5))
# bars = plt.bar(Teams, Tropies, color=colors, edgecolor='white',linewidth=1.5)
# plt.title("Tropues win by each Team")
# plt.ylabel("Number of tropies won")
# for bar,val in zip(bars,Tropies):
#     plt.text(bar.get_x()+bar.get_width()/2, val+30, str(val), ha='center',fontweight='bold')
# plt.tight_layout()
# plt.show()


import numpy as np

study_hrs = np.random.uniform(2,10,50)
marks = study_hrs * 7 + np.random.normal(0,8,50)
marks = np.clip(marks, 30, 100)

plt.figure(figsize=(8,5))
plt.scatter(study_hrs,marks, c=marks, cmap='RdYlGn', s=100, alpha=0.8)
plt.colorbar(label= 'Marks')
plt.title('study hours vs Exam hours')
plt.xlabel('study Hours/day')
plt.ylabel('Exam Marks')
plt.show()