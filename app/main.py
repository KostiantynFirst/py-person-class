class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:

    persons_list = [Person(name=person_data["name"],
                           age=person_data["age"])
                    for person_data in people]

    for persons, obj in zip(people, persons_list):
        wife_name = persons.get("wife")
        husband_name = persons.get("husband")
        if wife_name is not None:
            obj.wife = Person.people[wife_name]
        if husband_name is not None:
            obj.husband = Person.people[husband_name]

    return persons_list
