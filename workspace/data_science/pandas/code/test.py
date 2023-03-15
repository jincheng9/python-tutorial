import pandas

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pandas.DataFrame(mydataset)

print(myvar)

field = 'cars'

car_value = getattr(myvar, field)

print(type(car_value))
print(car_value)