import datetime

ivesta_data = input("Įveskite pirmą datą (pvz. 2023-05-01 13:50:00): ")
data1 = datetime.datetime.strptime(ivesta_data, "%Y-%m-%d %H:%M:%S")
now = datetime.datetime.now()

rezultatas = now - data1
metai = rezultatas.days / 365
menesiai = metai * 12
valandos = rezultatas.total_seconds() / 3600
minutes = rezultatas.total_seconds() / 60

print("Skirtumas metais: ", round(metai))
print("Skirtumas menesiai: ", round(menesiai))
print("Skirtumas dienomis: ", round(rezultatas.days))
print("Skirtumas valandomis: ", round(valandos))
print("Skirtumas minutemis: ", round(minutes))
print("Skirtumas sekundemis: ", round(rezultatas.total_seconds()))
