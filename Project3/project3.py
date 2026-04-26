import json

def add_person():
    name=input("Name: ")
    age=input("Age: ")
    email=input("Email: ")

    person={"name": name, "age":age,"email":email}
    return person
def display_people(people):
    if not people:
        print("No contacts found")
        return
    for i , person in enumerate(people):
        print(i+1,  "-" , person["name"],"|", person["age"],"|", person["email"])
def delete_contact(people):
    display_people(people)
    while True:
        number= input("Enter a number to delete")
        try:
            number=int(number)

            if number <=0 or number > len(people):
                print("Invalid Number, out of range")
            else:
                break
        except ValueError:
            print("Invalid Number")
    people.pop(number-1)
    print("person deleted")

def search(people):
    search_name=input("Search for a name: ").lower()
    results=[]

    for person in people:
        if search_name in person["name"].lower():
            results.append(person)

    display_people(results)

print("Hi, Welcome to the Contact Management System \n")
try:
    with open("contacts.json","r") as f:
        people=json.load(f)["contacts"]
except (FileNotFoundError,json.JSONDecodeError):
    people=[]

while True:
    print()
    print("Contact list size:", len(people))
    command=input("You can 'Add', 'Delete' or 'Search','List and 'Q' for Quit: ").lower()

    if command=="add":
        person= add_person()
        people.append(person)
        print("Person added! ")
    elif command=="delete":
        delete_contact(people)
    elif command=="search":
        search(people)
    elif command=="list":
        display_people(people)
    elif command=="q":
        break
    else:
        print("Invalid Command")

with open("contacts.json","w") as f:
    json.dump({"contacts": people},f, indent=4)