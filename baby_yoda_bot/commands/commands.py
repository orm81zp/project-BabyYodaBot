CMD_CHANGE_NOTE = "change note"
CMD_ADD_ADDRESS = "add address"
CMD_SHOW_ADDRESS = "show address"
CMD_REMOVE_ADDRESS = "remove address"
CMD_ADD_CONTACT = "add contact"
CMD_SEARCH_CONTACT = "search contact"
CMD_SHOW_CONTACT = "show contact"
CMD_ALL_CONTACTS = "all contacts"
CMD_REMOVE_CONTACT = "remove contact"
CMD_ADD_BIRTHDAY = "add birthday"
CMD_SHOW_BIRTHDAY = "show birthday"
CMD_REMOVE_BIRTHDAY = "remove birthday"
CMD_BIRTHDAYS = "birthdays"
CMD_ADD_EMAIL = "add email"
CMD_SHOW_EMAIL = "show email"
CMD_REMOVE_EMAIL = "remove email"
CMD_ADD_PHONE = "add phone"
CMD_SHOW_PHONE = "show phone"
CMD_CHANGE_PHONE = "change phone"
CMD_REMOVE_PHONE = "remove phone"
CMD_ADD_NOTE = "add note"
CMD_SHOW_NOTE = "show note"
CMD_CHANGE_NOTE = "change note"
CMD_SEARCH_NOTE = "search note"
CMD_REMOVE_NOTE = "remove note"
CMD_ALL_NOTES = "all notes"
CMD_SEARCH_BY_TAG = "search by tag"
CMD_ADD_TAG = "add tag"
CMD_REMOVE_TAG = "remove tag"
CMD_ALL_TAGS = "all tags"
CMD_HELP = "help"
CMD_CLOSE = "close"
CMD_EXIT = "exit"
EXIT_COMMANDS = [CMD_CLOSE, CMD_EXIT]

ARG_NOTE_ID = "note id"
ARG_NAME = "name"
ARG_PHONE = "phone"
ARG_TAGS = "tags"
ARG_TAG = "tag"
ARG_CONTENT = "content"
ARG_OLD_PHONE = "old phone"
ARG_NEW_PHONE = "new phone"
ARG_ADDRESS = "address"
ARG_EMAIL = "email"
ARG_BIRTHDAY = "birthday"
ARG_SEARCH = "search value"
ARG_BIRTHDAY_RANGE = "birthday range"

VALIDATION_RULES = {
    ARG_NAME: 'equivalent to "a-zA-Z0-9_.-", no spaces. Example: Max, J.Brain, Tom-1',
    ARG_PHONE: "can start with + and consist of 12 digits. Example: +380630000001",
    ARG_OLD_PHONE: f"same as for {ARG_PHONE}",
    ARG_NEW_PHONE: f"same as for {ARG_PHONE}",
    ARG_ADDRESS: "from 5 to 100 characters. Example: USA, 3944 D Street",
    ARG_EMAIL: "a valid email address. Example: max101@gmail.com",
    ARG_BIRTHDAY: 'a valid date, equivalent to "DD.MM.YYYY", future\'s date not accepted. Example: 24.06.2001',
    ARG_SEARCH: "case-insensitive characters. Example: hello world",
    ARG_BIRTHDAY_RANGE: "days range (7 by default) or a date (DD.MM). Example: 14, 15.02",
    ARG_TAG: "from 1 to 15 word characters",
    ARG_TAGS: "from 1 to 15 word characters separated by comma",
    ARG_CONTENT: "from 10 to 500 characters",
    ARG_NOTE_ID: "serial number of the note",
}

COMMAND_DESCRIPTION = {
    CMD_REMOVE_NOTE: "used to remove note",
    CMD_ADD_CONTACT: "used to add a new contact",
    CMD_ALL_CONTACTS: "used to display all contacts",
    CMD_SEARCH_CONTACT: "used to search contacts (case-insensitive)",
    CMD_SHOW_CONTACT: "used to display a contact",
    CMD_REMOVE_CONTACT: "used to remove a contact",
    CMD_ADD_BIRTHDAY: "used to add a birthday",
    CMD_SHOW_BIRTHDAY: "used to display a birthday",
    CMD_REMOVE_BIRTHDAY: "used to remove a birthday",
    CMD_ADD_PHONE: "used to add a phone",
    CMD_ADD_ADDRESS: "used to add an address",
    CMD_SHOW_ADDRESS: "used to display an address",
    CMD_ADD_EMAIL: "used to add an email",
    CMD_SHOW_EMAIL: "used to display an email",
    CMD_REMOVE_ADDRESS: "used to remove an address",
    CMD_REMOVE_EMAIL: "used to remove an email",
    CMD_SHOW_PHONE: "used to display a phone",
    CMD_CHANGE_PHONE: "used to change a phone",
    CMD_REMOVE_PHONE: "used to remove a phone",
    CMD_BIRTHDAYS: "used to display birthdays in coming days (7 by default)",
    CMD_ADD_NOTE: "used to add a note",
    CMD_SHOW_NOTE: "used to display a note",
    CMD_CHANGE_NOTE: "used to change a note",
    CMD_SEARCH_NOTE: "used to search notes by content",
    CMD_REMOVE_NOTE: "used to remove a note",
    CMD_ALL_NOTES: "used to display all notes",
    CMD_ADD_TAG: "used to add a tag(s)",
    CMD_SEARCH_BY_TAG: "used to display notes by a tag",
    CMD_REMOVE_TAG: "used to remove a tag(s)",
    CMD_ALL_TAGS: "used to display all tags",
}

ARGUMENT_TYPES = {
    "<required>": "required argument",
    "[optional]": "optional argument",
}
