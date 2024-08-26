from .decorator import input_error
from Assistant.classes import AddressBook, Record, View
import pickle


@input_error
def add_contact(args, book: AddressBook, view: View):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    view.display(message)


@input_error
def change_contact(args, book, view: View):
    name, old_phone, new_phone, *_ = args
    record = book.find(name)
    if record:
        record.edit_phone(old_phone, new_phone)
        view.display("Contact updated.")
    else:
        raise KeyError


@input_error
def show_phone(args, book, view: View):
    (name,) = args
    record = book.find(name)
    if record:
        view.display("; ".join([str(phone) for phone in record.phones]))
    else:
        raise KeyError


def show_all(book, view: View):
    view.display("\n".join([str(record) for record in book.data.values()]))


@input_error
def add_birthday(args, book, view: View):
    name = args[0]
    birthday = args[1]
    record = book.find(name)
    if record:
        record.add_birthday(birthday)
        view.display("Birthday added.")
    else:
        raise KeyError


@input_error
def show_birthday(args, book, view: View):
    (name,) = args
    record = book.find(name)
    view.display(str(record.birthday))


def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)


def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()  # Повернення нової адресної книги, якщо файл не знайдено
