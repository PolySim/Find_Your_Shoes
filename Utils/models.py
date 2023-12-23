from keras import *

from Utils.db import get_shoes

model = Sequential()
model.add(layers.Dense(units=3, input_shape=[6]))

model.add(layers.Dense(units=64))
model.add(layers.Dense(units=64))
model.add(layers.Dense(units=64))
model.add(layers.Dense(units=64))
model.add(layers.Dense(units=64))
model.add(layers.Dense(units=64))
model.add(layers.Dense(units=64))
model.add(layers.Dense(units=64))

model.add(layers.Dense(units=1))
model.compile(loss='mse', optimizer='adam')

request = get_shoes()

model.fit(request["request"], request["results"], epochs=100000, verbose=0)

model.save("model.h5")

while True:
    a = input("Enter a number: ")
    b = input("Enter a number: ")
    c = input("Enter a number: ")
    d = input("Enter a number: ")
    e = input("Enter a number: ")
    f = input("Enter a number: ")
    value = (int(a), int(b), int(c), int(d), int(e), int(f))
    print(model.predict([value]))
