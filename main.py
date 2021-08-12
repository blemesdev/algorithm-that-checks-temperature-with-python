from temperature import temperature

temp = temperature.Temperature()

t = temp.get_datas()
f = temp.convert_temperature();
temp.register_temperature();

print('Temperatura atual é:', t, "ºc")
print('Temperatura atual em Fahrenheit:', f, "ºf")
