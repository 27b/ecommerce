from slugify import slugify
from tools.database import db
from admin.models import Notification


def safe_url(value: str) -> dict:
    """ Receive string and return secure string for urls. """
    
    value_formated = {'status': None, 'result': None}
    
    try: 
        value_formated['status'] = True
        value_formated['result'] = slugify(value)

    except Exception as error:
        value_formated['status'] = False
        value_formated['result'] = error

    finally:
        return value_formated


def create_notification(title: str, information: str, link=None) -> dict:
    """ Create Notification in Admin panel. """
    
    status = {'status': None, 'result': None}

    try:
        if title and information:
            new_notification = Notification()
            new_notification.title = title
            new_notification.information = information

            if link: new_notification.link = link

            db.session.add(new_notification)
            db.session.commit()

            status['status'] = True
            status['result'] = new_notification

    except Exception as error:
        db.session.rollback()
        status['status'] = False
        status['result'] = error

    finally:
        return status

