from temperature import temperature

temp = temperature.Temperature()

t = temp.get_Datas()
f = temp.convert_temperature();

print('Temperatura atual é:', t, "ºc")
print('Temperatura atual em Fahrenheit:', f, "ºf")
