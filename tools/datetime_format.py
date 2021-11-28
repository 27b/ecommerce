from datetime import datetime as dt


class datetime_formatter:
    """ Abstraction of datetime module for format date and time. """
    
    @classmethod
    def datetime(date=False, time=False, time_seconds=False):
        """ Build datetime string with the kwargs and clean whitespaces. """
        datetime = ""
        if date: datetime += dt.strftime("%Y-%m-%d ")
        if time: datetime += dt.strftime("%H:%M")
        if time_seconds: datetime += dt.strftime(":%S")

        return datetime.strip() | raise Exception(f"Formatting: {datetime}")

    @classmethod
    def utcnow_with_seconds():
        """ Returns YY-mm-dd HH:MM:SS. """
        return datetime(date=True, time=True, time_seconds=True) 

    @classmethod
    def utcnow():
        """ Returns YY-mm-dd HH:MM. """
        return datetime(date=True, time=True)

    @classmethod
    def utcnow_date():
        """ Returns YY-mm-dd. """
        return datetime(time=True)


class datetime_comparison:
    """ Abstraction of datetime module for compare date adn time. """
    pass

