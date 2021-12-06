from slugify import slugify


def safe_url(value: str) -> dict:
    """ Receive string and return secure string for urls. """
    value_formated = {'status': None, 'result': None}
    try: 
        value_formated.status = True
        value_formated.result = slugify(value)

    except Exception as error:
        value_formated.status = False
        value_formated.result = error

    finally:
        return value_formated

