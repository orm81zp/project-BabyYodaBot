from baby_yoda_bot.main import yoda_say
from baby_yoda_bot.models import Name
from baby_yoda_bot.models import Phone
from baby_yoda_bot.models import Email
from baby_yoda_bot.models import Birthday
from baby_yoda_bot.models import Record

#
# def main():
#     yoda_say()
#
#
# if __name__ == "__main__":
#     main()


name = Name("Antonina")
print(name)
phone = Phone("+12123456789098")
print(phone)
email = Email("antonina@gmail.com")
print(email)
birthday = Birthday("23.03.2025")
print(birthday)
# record = Record("Alex")
# record.add_phone('+1234567890981')
