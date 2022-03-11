from uuid import uuid4
from datetime import datetime as dt
from common.email import send_email


class VerificateEmail:
    """ Singleton pattern for email verification

        An instance generates a global list, using the
        create_email_verification method and assigning an email as a
        parameter, it generates a dict with email, secret code and
        an expiration date.
    """

    __instance = None
    __waiting_list = []
    __expired_time = 15


    def __new__(cls):
        if VerificateEmail.__instance == None:
            VerificateEmail.__instnace = object.__new__(cls)
        return VerificateEmail.__instance

    @classmethod
    def __add_verification_to_list(cls, verification: dict) -> None:
        """ Add dict to waiting_list. """
        cls.__waiting_list.append(verification)

    @staticmethod
    def __generate_secret_code() -> str:
        """ Create a secret_code (used in safe urls). """
        return uuid4().hex


    @classmethod
    def set_expired_time(cls, time_in_minutes: int = 15) -> None:
        """ Set expired_time in items from waiting_list. """
        cls.__expired_time = time_in_minutes

    @classmethod
    def create_email_verification(cls, email: str) -> None:
        """ Create a dict with email, secret_code and datetime. """
        email = email
        secret_code = cls.__generate_secret_code()

        verification = {
            'email': email,
            'secret_code': secret_code,
            'expired': dt.utcnow + 5
        }

        cls.__add_verification_to_list(verification)

    @classmethod
    def verificate_email(cls, email: str, code: str) -> dict | None:
        """ Check list and clear old emails, if true return true and del. """
        # TODO: Check each element in the list, if the element is valid or
        # false do something
        for item in cls.__waiting_list:
            if item['datetime'] < dt.utcnow:
                cls.__waiting_list.remove(item)

            elif item['email'] == email and item['secret_code'] == code:
                tmp_item = item
                cls.__waiting_list.remove(item)
                return tmp_item

        return None

# EXAMPLE
# email_verification = VerificateEmail(15)
# email_verification(check_if_email_in_db)
#
# email = 'orionb@email.com'
# email_verification.create_email_verification(email)
#
#   verificate_email = email_verification.verificate_email(email)
#   
# if verificate_email:
#   verificate_email['email']

