# Baby Yoda's bot

## Description

A personal Baby Yoda's bot that helps you manage your contacts and notes.

## Table of Contents

-   [Installation](#installation)
-   [Basic functionality](#basic-functionality)
-   [Commands](#commands)

## Installation

### By GitHub

1. [Download ZIP](https://github.com/orm81zp/project-BabyYodaBot) from GitHub.
2. Extract the archive.
3. Install all dependencies `pip install -r requirements.txt`.
4. Go to the project folder and run `python3 test_baby_yoda.py`.

### By pip

Not availble yet

## Basic functionality

-   Save contacts with names, addresses, phone numbers, email and birthdays to the contact book.
-   Display a list of contacts whose birthday is a specified number of days from the current date.
-   Check the correctness of the entered phone number and email when creating or editing a record and notify the user in case of incorrect entry.
-   Search by contacts.
-   Edit and delete entries from the contact book.
-   Keep notes with text information.
-   Edit and delete notes.
-   Add and delete tags.
-   Search by notes or tags.

Can be restarted without losing data. All data (contacts, notes) are stored on the hard disk.

### Commands

Type `help` to see all commands. The example of the output is below:

```
add-contact               - used to add a new contact with all fields at once (wizard form): add-contact
change-contact            - used to change all conact's fields at once (wizard form): change-contact
search-contact            - used to search contacts by name, birthday, email, phone, address (case-insensitive): search-contact <search value>
show-contact              - used to display a contact: show-contact <name>
all-contacts              - used to display all contacts: all-contacts
remove-contact            - used to remove a contact: remove-contact <name>
add-birthday              - used to add a birthday: add-birthday <name> <birthday>
show-birthday             - used to display a birthday: show-birthday <name>
remove-birthday           - used to remove a birthday: remove-birthday <name>
birthdays                 - used to display birthdays that will happen in coming days (7 days by default): birthdays [days range]
add-address               - used to add an address: add-address <name> <address>
show-address              - used to display an address: show-address <name>
remove-address            - used to remove an address: remove-address <name>
add-email                 - used to add an email: add-email <name> <email>
show-email                - used to display an email: show-email <name>
remove-email              - used to remove an email: remove-email <name>
add-phone                 - used to add a phone: add-phone <name> <phone>
show-phone                - used to display a phone: show-phone <name>
change-phone              - used to change a phone: change-phone <name> <old phone> <new phone>
remove-phone              - used to remove a phone: remove-phone <name> <phone>
add-note                  - used to add a note: add-note <text>
show-note                 - used to display a note: show-note <note index>
change-note               - used to change a note: change-note <note index> <text>
search-note               - used to search notes by content (case-insensitive): search-note <search value>
remove-note               - used to remove a note: remove-note <note index>
all-notes                 - used to display all notes: all-notes
search-note-by-tag        - used to display all notes found by a tag (case-insensitive, strict match): search-note-by-tag <tag>
add-tag                   - used to add a tag: add-tag <note index> <tag>
remove-tag                - used to remove a tag (strict match): remove-tag <note index> <tag>
all-tags                  - used to display all tags: all-tags
show-tag                  - used to display tags in a note: show-tag <note index>
help                      - used to display information about all commands: help
close | exit              - used to close the program, data will be saved: close

Types of argumets:
<required>                - required argument
[optional]                - optional argument

Validation rules:
<name>                    - equivalent to "a-zA-Z0-9_.-", no spaces. Example: Max, J.Brain, Tom-1
<new name>                - same as for <name>
<phone>                   - begins with + and consist of 12 digits. Example: +380630000001
<old phone>               - same as for <phone>
<new phone>               - same as for <phone>
<address>                 - from 10 to 100 characters. Example: 3944 D Street
<email>                   - a valid email address. Example: max101@gmail.com
<note index>              - an existing index of a note, starts from 1
<tag>                     - from 1 to 15 word characters, equivalent to "a-zA-Z0-9_", no spaces. Example: shopping
<text>                    - from 10 to 500 characters
<birthday>                - a valid date, equivalent to "DD.MM.YYYY", no future's date of birth. Example: 24.06.2001
<search value>            - case-insensitive world characters. Example: hello world
[days range]              - (optional) a number of days (7 by default). Example: 14
```

### help

Used to display all commands: `help`.

### close or exit

use `close` or `exit` to close the program. The current data will be saved.

```
Enter a command: exit
Good bye!
✓ Contact book saved!
```
