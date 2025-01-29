class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list[Person]:
    persons = [Person(person["name"], person["age"]) for person in people]
    for person_data, person in zip(people, persons):
        if person_data.get("wife"):
            person.wife = Person.people.get(person_data["wife"])
        elif person_data.get("husband"):
            person.husband = Person.people.get(person_data["husband"])
    return persons
