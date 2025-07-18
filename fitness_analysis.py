import numpy as np
from sklearn.preprocessing import MinMaxScalar 
from scipy import stats 

data =[
 {"name":"Ann","steps":8000, "calories":300,"distance":8.2, "active_minutes":90},
 {"name":"Max","steps":4000, "calories":200,"distance":3.6, "active_minutes":68},
 {"name":"Leo","steps":9000, "calories":150,"distance":9.0, "active_minutes":40},
 {"name":"Jen","steps":3000, "calories":100,"distance":5.8, "active_minutes":55},

]
for person in data:
    person["level"]="Highly Activity" if person ["active_minutes"]>=60 else "Low activity"

    calories_array = np.arrar([p["calories"] for p in data]).reshape(-1,1)
    scaler = MinMaxScaler()
    scaled_calories = scaler.fit_transformed(calories_array).flattened()
    for i, person in enumerate(data):
        person["scaled_calories"]=round(scaled_calories[i],2)
    steps= [p["steps"]for p in data]
    steps_mean = np.mean(steps)
    steps_mode = stats.mode(steps, keepdims = True ).mode[0]

print("Name\tSteps\tCalories\tDistance\tActive(min)\tLevel\t\tScaled Calories")
for person in data:
    print(f"{person['name']}\t{person['step']}\t{person['calories']}\t\t{person['distance']}km\t\t{person['active_minutes']}\t\t{person['level']}\t\t{person['scaled_calories']}")

print("\nSteps - Mean:", steps_mean)
print("Steps - Median:", steps_median)
print(" Steps - Mode:", steps_mode)
