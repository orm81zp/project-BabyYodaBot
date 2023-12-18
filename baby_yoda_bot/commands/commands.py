CMD_ADD_ADDRESS = "add-address"
CMD_SHOW_ADDRESS = "show-address"
CMD_REMOVE_ADDRESS = "remove-address"
CMD_ADD_CONTACT = "add-contact"
CMD_SEARCH_CONTACT = "search-contact"
CMD_SHOW_CONTACT = "show-contact"
CMD_ALL_CONTACTS = "all-contacts"
CMD_REMOVE_CONTACT = "remove-contact"
CMD_ADD_BIRTHDAY = "add-birthday"
CMD_SHOW_BIRTHDAY = "show-birthday"
CMD_REMOVE_BIRTHDAY = "remove-birthday"
CMD_BIRTHDAYS = "birthdays"
CMD_ADD_EMAIL = "add-email"
CMD_SHOW_EMAIL = "show-email"
CMD_REMOVE_EMAIL = "remove-email"
CMD_ADD_PHONE = "add-phone"
CMD_SHOW_PHONE = "show-phone"
CMD_CHANGE_PHONE = "change-phone"
CMD_REMOVE_PHONE = "remove-phone"
CMD_ADD_NOTE = "add-note"
CMD_SHOW_NOTE = "show-note"
CMD_CHANGE_NOTE = "change-note"
CMD_SEARCH_NOTE = "search-note"
CMD_REMOVE_NOTE = "remove-note"
CMD_ALL_NOTES = "all-notes"
CMD_SEARCH_NOTE_BY_TAG = "search-note-by-tag"
CMD_ADD_TAG = "add-tag"
CMD_REMOVE_TAG = "remove-tag"
CMD_ALL_TAGS = "all-tags"
CMD_SHOW_TAG = "show-tag"
CMD_HELP = "help"
CMD_CLOSE = "close"
CMD_EXIT = "exit"
EXIT_COMMANDS = [CMD_CLOSE, CMD_EXIT]

ARG_NAME = "<name>"
ARG_NEW_NAME = "<new name>"
ARG_PHONE = "<phone>"
ARG_OLD_PHONE = "<old phone>"
ARG_NEW_PHONE = "<new phone>"
ARG_ADDRESS = "<address>"
ARG_EMAIL = "<email>"
ARG_NOTE_INDEX = "<note index>"
ARG_TAG = "<tag>"
ARG_TEXT = "<text>"
ARG_BIRTHDAY = "<birthday>"
ARG_SEARCH_VALUE = "<search value>"
ARG_DAYS_RANGE = "[days range]"

VALIDATION_RULES = {
    ARG_NAME: 'equivalent to "a-zA-Z0-9_.-", no spaces. Example: Max, J.Brain, Tom-1',
    ARG_PHONE: "begins with + and consist of 12 digits. Example: +380630000001",
    ARG_OLD_PHONE: f"same as for {ARG_PHONE}",
    ARG_NEW_PHONE: f"same as for {ARG_PHONE}",
    ARG_ADDRESS: "from 10 to 100 characters. Example: 3944 D Street",
    ARG_EMAIL: "a valid email address. Example: max101@gmail.com",
    ARG_NOTE_INDEX: "an existing index of a note, starts from 1",
    ARG_TAG: 'from 1 to 15 word characters, equivalent to "a-zA-Z0-9_", no spaces. Example: shopping',
    ARG_TEXT: "from 10 to 500 characters",
    ARG_BIRTHDAY: 'a valid date, equivalent to "DD.MM.YYYY", no future\'s date of birth. Example: 24.06.2001',
    ARG_SEARCH_VALUE: "case-insensitive world characters. Example: hello world",
    ARG_DAYS_RANGE: "(optional) a number of days (7 by default). Example: 14",
}

ARGUMENT_TYPES = {
    "<required>": "required argument",
    "[optional]": "optional argument",
}

COMMANDS = [
    {
        "commands": [CMD_ADD_CONTACT],
        "arguments": [],
        "description": "used to add a new contact with all fields at once (wizard form)",
    },
    {
        "commands": [CMD_SEARCH_CONTACT],
        "arguments": [ARG_SEARCH_VALUE],
        "description": "used to search contacts by name, birthday, email, phone, address (case-insensitive)",
    },
    {
        "commands": [CMD_SHOW_CONTACT],
        "arguments": [ARG_NAME],
        "description": "used to display a contact",
    },
    {
        "commands": [CMD_ALL_CONTACTS],
        "arguments": [],
        "description": "used to display all contacts",
    },
    {
        "commands": [CMD_REMOVE_CONTACT],
        "arguments": [ARG_NAME],
        "description": "used to remove a contact",
    },
    {
        "commands": [CMD_ADD_BIRTHDAY],
        "arguments": [ARG_NAME, ARG_BIRTHDAY],
        "description": "used to add a birthday",
    },
    {
        "commands": [CMD_SHOW_BIRTHDAY],
        "arguments": [ARG_NAME],
        "description": "used to display a birthday",
    },
    {
        "commands": [CMD_REMOVE_BIRTHDAY],
        "arguments": [ARG_NAME],
        "description": "used to remove a birthday",
    },
    {
        "commands": [CMD_BIRTHDAYS],
        "arguments": [ARG_DAYS_RANGE],
        "description": "used to display birthdays that will happen in coming days (7 days by default)",
    },
    {
        "commands": [CMD_ADD_ADDRESS],
        "arguments": [ARG_NAME, ARG_ADDRESS],
        "description": "used to add an address",
    },
    {
        "commands": [CMD_SHOW_ADDRESS],
        "arguments": [ARG_NAME],
        "description": "used to display an address",
    },
    {
        "commands": [CMD_REMOVE_ADDRESS],
        "arguments": [ARG_NAME],
        "description": "used to remove an address",
    },
    {
        "commands": [CMD_ADD_EMAIL],
        "arguments": [ARG_NAME, ARG_EMAIL],
        "description": "used to add an email",
    },
    {
        "commands": [CMD_SHOW_EMAIL],
        "arguments": [ARG_NAME],
        "description": "used to display an email",
    },
    {
        "commands": [CMD_REMOVE_EMAIL],
        "arguments": [ARG_NAME],
        "description": "used to remove an email",
    },
    {
        "commands": [CMD_ADD_PHONE],
        "arguments": [ARG_NAME, ARG_PHONE],
        "description": "used to add a phone",
    },
    {
        "commands": [CMD_SHOW_PHONE],
        "arguments": [ARG_NAME],
        "description": "used to display a phone",
    },
    {
        "commands": [CMD_CHANGE_PHONE],
        "arguments": [ARG_NAME, ARG_OLD_PHONE, ARG_NEW_PHONE],
        "description": "used to change a phone",
    },
    {
        "commands": [CMD_REMOVE_PHONE],
        "arguments": [ARG_NAME, ARG_PHONE],
        "description": "used to remove a phone",
    },
    {
        "commands": [CMD_ADD_NOTE],
        "arguments": [ARG_TEXT],
        "description": "used to add a note",
    },
    {
        "commands": [CMD_SHOW_NOTE],
        "arguments": [ARG_NOTE_INDEX],
        "description": "used to display a note",
    },
    {
        "commands": [CMD_CHANGE_NOTE],
        "arguments": [ARG_NOTE_INDEX, ARG_TEXT],
        "description": "used to change a note",
    },
    {
        "commands": [CMD_SEARCH_NOTE],
        "arguments": [ARG_SEARCH_VALUE],
        "description": "used to search notes by content (case-insensitive)",
    },
    {
        "commands": [CMD_REMOVE_NOTE],
        "arguments": [ARG_NOTE_INDEX],
        "description": "used to remove a note",
    },
    {
        "commands": [CMD_ALL_NOTES],
        "arguments": [],
        "description": "used to display all notes",
    },
    {
        "commands": [CMD_SEARCH_NOTE_BY_TAG],
        "arguments": [ARG_TAG],
        "description": "used to display all notes found by a tag (case-insensitive, strict match)",
    },
    {
        "commands": [CMD_ADD_TAG],
        "arguments": [ARG_NOTE_INDEX, ARG_TAG],
        "description": "used to add a tag",
    },
    {
        "commands": [CMD_REMOVE_TAG],
        "arguments": [ARG_NOTE_INDEX, ARG_TAG],
        "description": "used to remove a tag (strict match)",
    },
    {
        "commands": [CMD_ALL_TAGS],
        "arguments": [],
        "description": "used to display all tags",
    },
    {
        "commands": [CMD_SHOW_TAG],
        "arguments": [ARG_NOTE_INDEX],
        "description": "used to display tags in a note",
    },
    {
        "commands": [CMD_HELP],
        "arguments": [],
        "description": "used to display information about all commands",
    },
    {
        "commands": EXIT_COMMANDS,
        "arguments": [],
        "description": "used to close the program, data will be saved",
    },
]
