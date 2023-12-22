from collections import defaultdict
from datetime import datetime
from rich.console import Console
from rich.table import Table


class InvalidUserArgs(Exception):
    pass


class InvalidUserDateType(Exception):
    pass


WEEKDAYS = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}

LAST_WORK_DAY = 4  # Friday
DAYS_RANGE = 7


def get_weekday(weekday, use_work_days=True):
    """Takes the number of the week and returns the name of the week day or Monday if the weekday falls on a weekend

    Parameters:
        weekday (int): the number of the week, exp: 0

    Returns:
        str: the name of the week day, exp: Monday
    """
    if use_work_days:
        return WEEKDAYS[0] if weekday > LAST_WORK_DAY else WEEKDAYS[weekday]

    return WEEKDAYS[weekday]


def parse_user_data(user):
    """Checks required keys in user data and eirther returns name and birthday values or raise an exception

    Parameters:
        user (dict): exp: {"name": "Bill Gates", "birthday": datetime(1955, 11, 11)}

    Returns:
        tuple: exp: (\"Bill Gates\", datetime(1955, 11, 11)) or raise an exception
    """

    if not ("name" in user and "birthday" in user):
        raise InvalidUserArgs

    if not isinstance(user["birthday"], datetime):
        raise InvalidUserDateType

    name = user["name"]
    birthday = user["birthday"].date()
    return name, birthday


def get_birthdays(users, days_range=None, use_range=True, use_work_days=True):
    """Takes the list of users with required \"name\" and \"birthday\" keys and show them with birthdays one week ahead of the current day

    Parameters:
    users (list(dict)): the list of dicts, exp: [{"name": "Bill Gates", "birthday": datetime(1955, 11, 11)}]

    Output:
    displays birthdays one week ahead of the current day, exp: Monday: Bill Gates
    """

    if days_range is None:
        days_range = DAYS_RANGE

    today = datetime.today().date()
    grouped_birthdays = defaultdict(list)

    for user in users:
        try:
            name, birthday = parse_user_data(user)
            birthday_this_year = birthday.replace(year=today.year)

            if birthday_this_year < today:
                birthday_this_year = birthday.replace(year=today.year + 1)

            delta_days = (birthday_this_year - today).days

            if delta_days < days_range or not use_range:
                birthday_weekday = birthday_this_year.weekday()
                weekday = get_weekday(birthday_weekday, use_work_days)
                grouped_birthdays[weekday].append(name)

        except InvalidUserArgs:
            print('Not found required "name" and "birthday" keys.')
        except InvalidUserDateType:
            print("Birthday value must be a datetime type.")
        except Exception as err:
            print(f"\u02DF Oops! Something went wrong, {err}")

    if len(grouped_birthdays) > 0:
        print()
        title = ":party_popper: Birthdays"
        table = Table(title=title, header_style="bright_green", min_width=80)
        table.add_column("Weekday", min_width=10)
        table.add_column("Contacts")

        for weekday, users_list in grouped_birthdays.items():
            table.add_row(weekday, ", ".join(users_list))

        Console().print(table)
        print()
    else:
        print("Nothing to display.")


__all__ = ["get_birthdays"]
