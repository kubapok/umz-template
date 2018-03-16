#!/bin/python3
import pandas as pd
import matplotlib.pyplot as plt
flats = pd.read_csv('train/train.tsv', sep = '\t',
                   names = ['price', 'isNew','rooms', 'floor', 'location', 'sqrMetres'])
from sklearn import linear_model

reg = linear_model.LinearRegression()

X = flats['sqrMetres']
X = X.values.reshape(-1,1)
Y = flats['price']

model = reg.fit(X, Y)

a = model.coef_[0]
b = model.intercept_

print('y= {0}x + {1}'.format(a,b))

plt.scatter(X,Y, color='orange')
plt.plot([0,200],[b,a*200+b], 'r')
plt.title('Linear regression')
plt.xlabel('sqrMetres')
plt.ylabel('price')
plt.show()
