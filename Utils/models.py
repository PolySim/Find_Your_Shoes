from keras import *

model = Sequential()
model.add(layers.Dense(units=3, input_shape=[2]))

model.add(layers.Dense(units=64))
model.add(layers.Dense(units=64))
model.add(layers.Dense(units=64))

model.add(layers.Dense(units=1))
model.compile(loss='mse', optimizer='adam')

X_train = [(1, 3), (4, 8), (3, -2), (4, 19), (5, 25)]
y_train = [4, 12, 1, 23, 30]

model.fit(X_train, y_train, epochs=1000, verbose=0)

while True:
    x = input("Enter a number: ")
    y = input("Enter a number: ")
    value = (float(x), float(y))
    print(model.predict([value]))
