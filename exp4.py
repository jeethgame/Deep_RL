import numpy as np
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense

X = np.array([[0], [1], [2], [3]])
y = np.array([0, 1, 2, 3])

m = Sequential([Dense(4, activation='relu', input_shape=(1,)), Dense(1)])
m.compile(optimizer='adam', loss='mse')
m.fit(X, y, epochs=100, verbose=0)

print(m.predict(X, verbose=0).round(2))