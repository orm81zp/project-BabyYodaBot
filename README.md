# Baby Yoda Bot

## Description

Your personal Baby Yoda Bot that helps you manage your contacts and notes.

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

Available on [test.pypi.org](https://test.pypi.org/project/baby-yoda-bot/) only for academic purposes.

The latests Alpha version

```
pip install --index-url https://test.pypi.org/simple/ baby-yoda-bot
```

_Add `--no-deps` option if you don't want to install all package dependencies._

```
pip install --index-url https://test.pypi.org/simple/ --no-deps baby-yoda-bot
```

## How to run

From the code

```
from baby_yoda_bot import yoda_say

yoda_say()
```

or directly from the terminal running `yoda_bot` after installation from pip.

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
add-contact               - used to add a new contact: add-contact
all-contacts              - used to display all contacts: all-contacts
search-contact            - used to search contacts (case-insensitive): search-contact
show-contact              - used to display a contact: show-contact
remove-contact            - used to remove a contact: remove-contact
add-birthday              - used to add a birthday: add-birthday
show-birthday             - used to display a birthday: show-birthday
remove-birthday           - used to remove a birthday: remove-birthday
add-phone                 - used to add a phone: add-phone
add-address               - used to add an address: add-address
show-address              - used to display an address: show-address
add-email                 - used to add an email: add-email
show-email                - used to display an email: show-email
remove-address            - used to remove an address: remove-address
remove-email              - used to remove an email: remove-email
show-phone                - used to display a phone: show-phone
change-phone              - used to change a phone: change-phone
remove-phone              - used to remove a phone: remove-phone
birthdays                 - used to display birthdays in coming days (7 by default) or by a date (DD.MM): birthdays
add-note                  - used to add a note: add-note
show-note                 - used to display a note: show-note
all-notes                 - used to display all notes: all-notes
change-note               - used to change a note: change-note
remove-note               - used to remove a note: remove-note
search-note               - used to search notes by content (case-insensitive): search-note
search-by-tag             - used to display all notes found by a tag (case-insensitive, strict match): search-by-tag
add-tag                   - used to add a tag: add-tag
remove-tag                - used to remove a tag (strict match): remove-tag
all-tags                  - used to display all tags with associated notes: all-tags
save                      - used to save data: save
help                      - used to display information about all commands: help
close | exit              - used to close the program, data will be saved: close

Validation rules:
name                      - from 1 to 30 characters. Example: Max, John Doe, Erika from the gym
phone                     - can begin with + and consist of 12 digits. Example: +380630000001
old phone                 - same as for <phone>
new phone                 - same as for <phone>
address                   - from 5 to 100 characters. Example: USA Brooklyn, state Michigan, 3854 Central Avenue
email                     - a valid email address. Example: maxi21@gmail.com
Note Id                   - a sequence number, starts from 1
tag                       - from 1 to 15 word characters, no spaces, can be a list separeted by space. Example: shopping buy food
text                      - from 10 to 500 characters
birthday                  - a valid date, equivalent to "DD.MM.YYYY", no future's date of birth. Example: 24.06.2001
birthday range            - a number of days or a date (DD.MM). Example: 14, 01.12
search                    - case-insensitive world characters. Example: Hello World
```

### Some examples of the use of commands

### help

Used to display all commands: `help`.

### add-phone

Used to add a phone: `add-phone`.

```
Enter name: Maxima
Enter phone: +380660000001
Contact "Maxima" added!
Phone number added!
```

### change-phone

used to change a phone: `change-phone`.

```
Enter command: change-phone
(Press Control + C to exit from menu)
Enter name: Maxima
Enter old phone: +380660000001
Enter new phone: +380663330001
Phone number updated!
```

### add-birthday

Used to add a birthday: `add-birthday`. Will be replaced if already exists.

```
Enter command: add-birthday
(Press Control + C to exit from menu)
Enter name: Maxima
Enter birthday: 12.12.2001
Birthday added!
```

### add-email

Used to add an email: `add-email`. Will be replaced if already exists.

```
Enter command: add-email
(Press Control + C to exit from menu)
Enter name: Maxima
Enter email: max21@gmail.com
Email added!
```

### add-address

Used to add an address: `add-address`. Will be replaced if already exists.

```
Enter command: add-address
(Press Control + C to exit from menu)
Enter name: Maxima
Enter address: Ukraine, Lviv
Address added!
```

### all-contacts

Used to display all contacts: `all-contacts`.

```
Enter command: all-contacts

                                             ⚔ All Contacts
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┓
┃ Name                  ┃ Phone              ┃ Birthday       ┃ Email                ┃ Address          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━┩
│ Maxima                │ +380663330001      │ 12.12.2001     │ max21@gmail.com      │ Ukraine, Lviv    │
│ John Woo              │ +380500000100      │ 10.10.1982     │ woo@gmail.com        │  -               │
└───────────────────────┴────────────────────┴────────────────┴──────────────────────┴──────────────────┘
```

### remove-contact

Used to remove a contact: `remove-contact`.
You need to confirm with "yes" or "y".

```
Enter command: remove-contact
(Press Control + C to exit from menu)
Enter name: Maxima
Contact Maxima will be removed, continue? (y/no) y
Contact deleted!
```

### birthdays

Used to display birthdays that will happen in some days (7 days by default): `birthdays`.

The example of the output:

```
                                  🎉 Birthdays
┏━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Weekday           ┃ Contacts                                                 ┃
┡━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Thursday          │ 10.10.1982 John Woo, 10.10.1984 Erika                    │
│ Monday            │ 25.12.1999 Steven Seagal                                 │
└───────────────────┴──────────────────────────────────────────────────────────┘
```

The example of the output for a particular date:

```
Enter command: birthdays
(Press Control + C to exit from menu)
Enter days range (7 by default) or a date (DD.MM): 10.10

                                  🎉 Birthdays
┏━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Weekday           ┃ Contacts                                                 ┃
┡━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Thursday          │ 10.10.1982 John Woo, 10.10.1984 Erika                    │
└───────────────────┴──────────────────────────────────────────────────────────┘
```

### add-note

Used to add a note: `add-note`.

```
Enter command: add-note
(Press Control + C to exit from menu)
Enter content: Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown
printer took a galley of type and scrambled it to make a type specimen book.
Enter tags, separated only by commas or spaces (optional): lorem dummy
Note added!
```

### all-notes

Used to display all notes: `all-notes`

```
Enter command: all-notes

                                                  ⚔ All Notes
┏━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┓
┃ Id         ┃ Content                                                                          ┃ Tags         ┃
┡━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━┩
│ 2          │ Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem │ dummy, lorem │
│            │ Ipsum has been the industry's standard dummy text ever since the 1500s, when an  │              │
│            │ unknown printer took a galley of type and scrambled it to make a type specimen   │              │
│            │ book.                                                                            │              │
└────────────┴──────────────────────────────────────────────────────────────────────────────────┴──────────────┘
```

#### close or exit

use `close` or `exit` to close the program. The current data will be saved.

```
Enter command: exit
Goodbye! See you later...
```
