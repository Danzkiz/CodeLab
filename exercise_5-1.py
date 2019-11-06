# Create a function that generates a person
import random

first_names = ['olga', 'peter', 'paul', 'indre', 'margarida', 'isabella', 'mathilde', 'bjorn']
locations = ['copenhagen', 'london', 'barcelona', 'reykjavik', 'brussels']

def create_person():
    first_name = random.choice(first_names)
    location = random.choice(locations)

    age = random.randint(12, 57)

    return { "name": first_name, "location": location, "age": age}


person1 = create_person()

#print(person1)


# Using the function above, create 20 people, put them in a list, and return it

def create_party(size: int):
    people = []
    for i in range(size):
        people.append(create_person())

    return people


party_people = create_party(size=20)

#for key in party_people:
#    print(key)

# Find all the people in a given location

def filter_by_location(location, people):
    people_in_correct_location = []
    for person in people:
        if location in person['location']:
            people_in_correct_location.append(person)
            #print(person)

    return people_in_correct_location


def filter_by_age(minimum_age: int, people):
    people_having_correct_age = []
    for person in people:
        if minimum_age <= person['age']:
            people_having_correct_age.append(person)

    return people_having_correct_age

guests = filter_by_location('copenhagen', party_people)

guest_age = filter_by_age(18, guests)

#print("These people are near by")
#print(guests)
#print("These people are old enough")
#print(guest_age)

# You need to buy supplies for the party
# Every person you've invited needs 3 drinks
# Based on a given location, find out how many drinks you should get
# Extra points: don't buy drinks for minors (age < 18)
# Extra extra points: people from reykjavik and brussels drink a lot, when given that location, buy 5 drinks for party goers

def calculate_number_of_drinks(age, location, people):
    people_matching_location = filter_by_location(location, people)
    people_matching_age = filter_by_age(age, people_matching_location)
    number_of_people = len(people_matching_age)
    number_of_drinks = 0

    if location == 'reykjavik' or location == 'brussels':
        number_of_drinks = number_of_people * 5
    else:
        number_of_drinks = number_of_people * 3

    return number_of_drinks


count_drinks = calculate_number_of_drinks(18, 'copenhagen', party_people)

print( "You should buy " + str(count_drinks) + " drinks for the party.")
