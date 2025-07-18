appliances  = [
    {"name":"Refrigerator","power":1.2,"hours":24,"efficient":"Yes"},
    {"name":"Washing Machine","power":0.5,"hours":1.5,"efficient":"Yes"},
    {"name":"Heater","power":2.0,"hours":5,"efficient":"No"},
    {"name":"Microwave","power":1.0,"hours":0.5,"efficient":"Yes"},
    {"name":"Air Conditioner","power":1.8,"hours":6,"efficient":"No"},

]
min_power = min(item["power"] for item in appliances)
max_power = max(item["power"] for item in appliances)

highest_appliance = max(appliances, key=lambda x: x["power"])
print ("Highest power usages appliance:", highest_appliance["name"])

for item in appliances:
    if item["power"]>2.5:
        item["Lable"]="Heavy Usage"
    else:
        item["Lable"]= "Efficient"   

total_power =sum(item["power"] for item in appliances)
average_power = round(total_power/ len(appliances),2)
print("Average Power Used:", average_power )

for item in appliances:
    print(item)
