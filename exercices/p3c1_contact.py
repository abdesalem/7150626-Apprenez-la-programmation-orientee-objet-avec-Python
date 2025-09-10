"""Contacts.

Séparez le programme en plusieurs modules et packages,
en ajoutant les fichiers __init__.py et les imports si necessaire.

Vérifiez que le programme s'éxecute correctement en lancant main.py depuis la racine
du projet.
"""

from exercices.contact import OwlContactSystem, TextContactSystem


class User:
    """Un utilisateur."""

    def __init__(self, name, contact_method):
        """Initialise un nom et une methode de contact."""
        self.name = name
        self.contact_method = contact_method

    def send(self, message):
        """Envoit un message."""
        self.contact_method.send(message)



# Our main program.
alice = User("Alice", TextContactSystem("0102030405"))
bob = User("Bob", OwlContactSystem("4 Privet Drive"))

user_list = [alice, bob]
super.send_mass_messages("Hello {name}, Comment vas-tu?", user_list)
super.send_mass_messages(
    "Salut {name}. Tes informations de contact sont-elles corrects?"
    " Nous avons celles-ci: {contact_info}.",
    user_list,
)
