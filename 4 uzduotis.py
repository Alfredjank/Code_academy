import datetime

while True:
    ivesta_data = input("Įveskite pirmą datą (pvz. 1991-01-01 12:45:12): ")
    try:
        data1 = datetime.datetime.strptime(ivesta_data, "%Y-%m-%d %H:%M:%S")
        break
    except ValueError:
        print("Įvedėte ne tinkama formatą, bandykite dar kartą")

while True:
    ivesta2_data = input("Įveskite antrą datą (pvz. 1991-01-01 12:45:12): ")
    try:
        data2 = datetime.datetime.strptime(ivesta2_data, "%Y-%m-%d %H:%M:%S")
        break
    except ValueError:
        print("Įvedėte ne tinkama formatą, bandykite dar kartą")

data1 = datetime.datetime.strptime(ivesta_data, "%Y-%m-%d %H:%M:%S")
data2 = datetime.datetime.strptime(ivesta2_data, "%Y-%m-%d %H:%M:%S")

skirtumas = data1 - data2

print("Tarp įvestų datų praėjo: ", abs(skirtumas.total_seconds()), "s", type(skirtumas))
