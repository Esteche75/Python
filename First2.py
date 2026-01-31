import json
import os

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Välkommen {self.name}. Du är {self.age} år gammal.")

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data["name"],
            age=data["age"],
        )


def create_user():
    name = input("Namn: ")
    age = int(input("Ålder: "))
    user = Person(name, age)
    return user


def save_users(users, filename="users.json"):
    data = [user.to_dict() for user in users]
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_users(filename="users.json"):
    if not os.path.exists(filename):
        return []

    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)

    users = [Person.from_dict(item) for item in data]
    return users


def main():
    users = load_users()

    while True:
        print("\n--- MENY ---")
        print("1. Lägg till användare")
        print("2. Lista användare")
        print("3. Spara och avsluta")

        choice = input("Val: ")

        if choice == "1":
            user = create_user()
            users.append(user)
        elif choice == "2":
            print("\nAnvändare:")
            if not users:
                print("Inga användare ännu.")
            for u in users:
                print(f"- {u.name} ({u.age} år)")
        elif choice == "3":
            save_users(users)
            print("Sparar och avslutar...")
            break
        else:
            print("Ogiltigt val, försök igen.")


if __name__ == "__main__":
    main()

