from .Commands.AddContact import AddContact
from .Commands.ShowContact import ShowContact
from .Commands.RequestInput import RequestInput


class BotLogic:
    def requestCommand(self):
        inp = RequestInput()

        return inp.value

    def add_contact(self, args):
        AddContact(args)

    def show_help(self):
        print('I can run only "add-contact", "all-contacts" or "exit"')

    # //робота із notes
    def show_all(self):
        ShowContact()

        # note = self.notes.find_note({'name'='Alex','description'....})
        # note = note.show('teest@gmail.com')
        # note = note.find('tag'='plant')
        # self.notes.save(record)
