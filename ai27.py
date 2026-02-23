import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
# x = np.linspace(-10, 10, 100)
# y = x**2
# ax.plot(x, y, label='y = x^2', color='violet')
# ax.set_title("Do thi y = x^2: ")
# ax.set_xlabel("x")
# ax.set_ylabel("y")


# days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
# temperatures = [22, 24, 25, 23, 26, 28, 27]
# ax.plot(days, temperatures, color='red', linestyle='--', marker='o', label='Weekly Temperature')
# ax.set_xlabel('Day')
# ax.set_ylabel('Temperature °C')


# data = np.random.normal(0,1,1000)
# plt.hist(data,bins=30,density=True,alpha=0.7,color='green',edgecolor='black')


# x = np.linspace(0, 10, 100)
# y1 = np.sin(x)
# y2 = np.cos(x)
# ax.plot(x,y1,color='blue',label='sin(x)')
# ax.plot(x,y2,color='red',label='cos(x)')


quarters = ['Q1', 'Q2', 'Q3', 'Q4']
sales_2022 = [120, 135, 145, 160]
sales_2023 = [130, 148, 155, 170]
x = np.arange(len(quarters))
w = 0.4

plt.bar(x-0.2,sales_2022,width=w-0.1,label='2022',color='blue')
plt.bar(x+0.2,sales_2023,width=w-0.1,label='2023',color='red')

ax.grid(True)
plt.title("Quarterly Sales Comparison")

ax.set_xticks(x)
ax.set_xticklabels(quarters)

ax.legend()

plt.tight_layout()
plt.show()