from datetime import datetime as dt


class datetime_generator:
    """ Abstraction of datetime module for format date and time. """
    
    @classmethod
    def _datetime(cls, date=None, time=None, time_seconds=None):
        """ Build datetime string with the kwargs and clean whitespaces. """
        datetime = ""
        utcnow = dt.utcnow()
        if date: datetime += utcnow.strftime("%Y-%m-%d ")
        if time: datetime += utcnow.strftime("%H:%M")
        if time_seconds: datetime += utcnow.strftime(":%S")

        return datetime.strip() #  | raise Exception(f"Formatting: {datetime}")

    @classmethod
    def utcnow_with_seconds(cls) -> str:
        """ Returns YY-mm-dd HH:MM:SS. """
        return cls._datetime(date=True, time=True, time_seconds=True) 

    @classmethod
    def utcnow(cls) -> str:
        """ Returns YY-mm-dd HH:MM. """
        return cls._datetime(date=True, time=True)

    @classmethod
    def utcnow_date(cls) -> str:
        """ Returns YY-mm-dd. """
        return cls._datetime(time=True)


class datetime_comparison:
    """ Abstraction of datetime module for compare date adn time. """
    pass

if __name__ == '__main__':
    print(datetime_generator.utcnow_with_seconds())
    print(datetime_generator.utcnow())
    print(datetime_generator.utcnow_date())

