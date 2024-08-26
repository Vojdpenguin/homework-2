from Comparser import parse_input
from processing import (
    add_contact,
    change_contact,
    show_phone,
    add_birthday,
    show_birthday,
    save_data,
    load_data,
    show_all,
)
from classes import ConsoleView
from pathlib import Path
import pickle

file_path = Path("database.bin")


def main():
    view = ConsoleView()
    book = load_data()
    view.display("Welcome to the assistant bot!")
    while True:
        user_input = view.input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            view.display("Good bye!")
            with open(file_path, "wb") as file:
                pickle.dump(book, file)
            break

        elif command == "hello":
            view.display("How can I help you?")

        elif command == "add":
            add_contact(args, book, view)

        elif command == "change":
            change_contact(args, book, view)

        elif command == "phone":
            show_phone(args, book, view)

        elif command == "all":
            show_all(book, view)

        elif command == "add-birthday":
            add_birthday(args, book, view)

        elif command == "show-birthday":
            show_birthday(args, book, view)

        elif command == "birthdays":
            birthdays = book.get_upcoming_birthdays()
            if not len(birthdays):
                view.display("There are no upcoming birthdays.")
                continue
            for day in birthdays:
                view.display(f"{day}")

        else:
            view.display("Invalid command.")
    save_data(book)


if __name__ == "__main__":
    main()
