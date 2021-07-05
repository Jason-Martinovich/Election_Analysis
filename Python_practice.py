counties = ["Arapahoe", "Denver", "Jefferson"]
print(counties)
print(counties[0])
print(counties[2])
print(counties[-1])
print(len(counties))
print(counties[0 : 2])
counties.append("El Paso")
print(counties)
counties.insert(2, "El Paso")
print(counties)
counties.remove("El Paso")
print(counties)
counties.pop(3)
print(counties)
counties[2] = 'El Paso'
print(counties)
counties[2] = 'Jefferson'
print(counties)
counties.insert(1, "El Paso")
print(counties)
counties.remove("Arapahoe")
counties[1] = "Denver"
counties.pop(2)
print(counties)
counties.insert(1, "Jefferson")
print(counties)
counties.append("Arapahoe")
print(counties)
counties.pop(0)
counties.insert(0, "Arapahoe")
counties.pop(3)
print(counties)
counties.insert(1, "Denver")
counties.pop(2)
print(counties)
counties.remove("Denver")
print(counties)
counties.append("Jefferson")
print(counties)
counties_tuple =("Arapahoe", "Denver", "Jefferson")
print(len(counties_tuple))
print(counties_tuple[1])

counties_dict = dict()
counties_dict["Arapahoe"] = 422829
print(counties_dict)
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
print(counties_dict)
print(len(counties_dict))
print(counties_dict.items())
print(counties_dict.keys())
print(counties_dict.values())
print(counties_dict.get("Denver"))
print(counties_dict["Arapahoe"])
voting_data = []
voting_data.append({"County":"Arapahoe" , "Registered_voters": 422829})
voting_data.append({"County":"Denver" , "Registered_voters": 463353})
voting_data.append({"County":"Jefferson" , "Registered_voters": 432438})
print(voting_data)

print(counties)

if counties[1]  == 'Denver':
    print(counties[1])

if "Arapahoe" in counties: 
    print("True")
else: print("False")

if "El Paso" not in counties:
    print("True")
else: print("False")

if "El Paso" in counties:
    print('El Paso is in the list of counties')
else:
    print("El Paso is not in the list of counties")

if  "Arapahoe" in counties or 'El Paso' in counties:
    print("Arapahoe and El Paso is in the list of counties")
else:
    print("Arapahoe or El Paso is not in the list of counties")

if "Arapahoe" in counties and "El Paso" not in counties:
    print("Only Arapahoe is in the list of counties")
else:
    print('Arapahoe is in the list of counties and El Paso is not in the list')

for county in counties:
    print(county)

numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)

for num in range(5):
    print(num)

for i in range(len(counties)):
    print(counties[i])

for county in counties_dict:
    print(county)

for county in counties_dict.keys():
    print(county)

for voters in counties_dict.values():
    print(voters)

for county in counties_dict:
    print(counties_dict.get(county))

for county, voters in counties_dict.items():
    print(county,voters)

for county, voters in counties_dict.items():
    print(county, "county has", voters, "registered voters.")

for counties_dict in voting_data:
    print(counties_dict)

for counties_dict in voting_data:
    for value in counties_dict.values():
        print(value)

counties_dict = {"Arapahoe": 369237, "Denver": 413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters. ")

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters")

candidate_votes = int(input("How many votes did the candidate get in the election?"))
total_votes = int(input("What is the total number of votes in th election?"))
message_to_candidate = (
    f"you received {candidate_votes} number of votes."
    f" The total number of votes in the election was {total_votes}."
    f" You recived {candidate_votes/total_votes * 100:.2f} % of the total votes.")
print(message_to_candidate)
