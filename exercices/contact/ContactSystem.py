from abc import ABC, abstractmethod

class ContactSystem(ABC):
    """Classe abstraite utilisée pour envoyer un message à un utilisateur."""

    @abstractmethod
    def send(self, message):
        """Toutes les sous-classes de ContactSystem doivent implémenter send."""
        pass

    def varify_address(address):
        """Fausse fonction qui retourne True."""
        return True

    def validate_phone(phone_number):
        """Retourne True par défaut."""
        return True


    def send_mass_messages(message, user_list):
        """Envoi des messages en masse.

        Utilise la méthode de message de chaque utilisateur."""
        for user in user_list:
            mail_merge = {"name": user.name, "contact_info": user.contact_method}
            customised_message = message.format(**mail_merge)
            user.send(customised_message)