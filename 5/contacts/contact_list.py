from contact import Contact


# ContactList is a custom class which stores only an instances of class Contact.
# It does not support methods of built-in `list` data type
# (since it's not inherited from it, so the only thing related to the lists is actually a class name)
# Python does not care about class names, it's for people more.
# But Python cares about protocols.
# If you want to say that something is a list to Python, that something should have specific methods implemented.
# If you implement special methods required for Iterator Protocol, for example,
# you will be able to do for loops with your custom list.


class ContactList:
    def __init__(self):
        self.storage = []
        self.index = 0

    def append(self, contact):
        if not isinstance(contact, Contact):
            raise ValueError('Invalid contact!')
        print(f'Save contact {contact} to the storage')
        self.storage.append(contact)

    def __str__(self):
        print(f'Contact stored: {len(self.storage)}')
        print('-' * 10)
        for contact in self.storage:
            print(contact)
        print('-' * 10)

    # Remember I told, that if you want to print your custom class nicely,
    # you need to defined __str__ method and tell python what to print exactly.

    # Read this section: https://realpython.com/python-iterators-iterables/#what-is-the-python-iterator-protocol

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.storage):
            contact = self.storage[self.index]
            self.index += 1
            return contact
        else:
            self.index = 0
            raise StopIteration


if __name__ == '__main__':
    contact_list = ContactList()
    mike = Contact(name='Mike', email='mike@example.com', age=30)

    # should append only instances of Contact class
    contact_list.append(mike)

    # should print list of contacts nicely as well as total amount
    print(contact_list)

    # should print each contact nicely
    for contact in contact_list:
        print(contact)
