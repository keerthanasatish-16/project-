pets =[
 {"Name":"Bolt","Type":"Dog","Age":2,"Vaccinated":"Yes","Status":"Available"},
 {"Name":"Max","Type":"Cat","Age":2,"Vaccinated":"No","Status":"Adopted"},
 {"Name":"Leo","Type":"Rabbit","Age":2,"Vaccinated":"Yes","Status":"Available"},
 {"Name":"Rocky","Type":"Dog","Age":2,"Vaccinated":"No","Status":"Adopted"},
 {"Name":"Tan","Type":"Dog","Age":2,"Vaccinated":"Yes","Status":"Available"},


]
def filter_pets_by_type(pet_list, pet_type):
    result = []
    for pet in pet_list:
        if pet ["Type"].lower()== pet_type.lower():
            result.append(pet)
            return result 
        
selected_type = "Dog"
dogs = filter_pets_by_type(pets, selected_type)

print(f"All{selected_type}s in shelter:")
for d in dogs:
    print(d)

def average_age_of_available_pets(pet_list):
    total_age = 0
    count = 0
    for pet in pet_list:
       if pet ["Status"].lower() == "available":
           total_age += pet["Age"]
           count += 1
           if count >0:
               return total_age/count
           else:
               return 0
avg_age = average_age_of_available_pets(pets)
print(f"nAvesrage age of avaible pets: {avg_age:2f} years")           
