import requests
import pandas as pd
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 10, 5, 10, 2]

plt.plot(x, y, marker='1')

plt.title('график')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)

plt.show()
print("\n код matplotlib  \n")

Data = [1, 3, 4, 5, 6, 2, 9]
s = pd.Series(Data)
Index = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
si = pd.Series(Data, Index)
print(si)
print("\n код pandas  \n")

response = requests.get('https://api.github.com')
print(response.json())
print("\n код requests \n")