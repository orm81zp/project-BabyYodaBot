### Dev Wiki

#### How to declare new bot command

Bot listens to commands from 
```baby_yoda_bot/bot/commands``` folder.
Each command should be imported into ```baby_yoda_bot/bot/commands/__init__.py```

Command is a function decorated via Bot class decorators.
The functions gets Context instance as the first argument and cmd args list as the second one

```python
@Bot.command('all-contacts')
def all_contacts(ctx: Context):
    ctx.adderss_book.do_something()

```

Once it declared and imported into ```baby_yoda_bot/bot/commands/__init__.py``` bot calls this function
if user run it in cmd:

```Enter command: all-contacts```

To add data inputs and validations, use following decorators:

- Bot.command - map command to cmd call (each command should be wrapped by)
- Bot.description - add command description into help output
- Bot.questions - add cmd wizard which asks step by step question from declration
- Bot.arguments - validates cmd arguments for command, e.g. for cal ```add-phone Igor 999999999999```


#### @Bot.command
That decorators just maps cmd call to corresponding function


#### @Bot.questions
Decorator sets wizard mod for command input and validates the arguments according to provided rules.

```python
@Bot.command('add-contact')
@Bot.description('used to add a contact')
@Bot.questions([
    {
        # arument name in the cmd prompt
        # e.g. Enter name:
        'name': 'name', 
        
        # shows if argument required, True by default.
        # if set to False => user is able skip the wizard step by pressing the ENTER
        # is user skips the step, than argument value is None
        'required': True,
        
        # class which validates the data.
        # it equals to str by default
        # if class throws ValidationValueException, exception message is shown to the user 
        'type': Name
    },
    {
        'name': 'phone',
        'required': False,
        'type': Phone
    },
    {
        'name': 'birthday',
        'required': False,
        'type': Birthday
    },
    {
        'name': 'email',
        'required': False,
        'type': Email,
    }
])
def add_contact(ctx: Context, args):
  """
    As that funciton uses 4 arguments,
    in the args array there are:
  """

  name, phone, birthday, email = args
  """
  name = instance of Name class
  phone - instance of Phone class
  birthday - instance of Birthday class
  email = instance of Email class

  If user skips the wizard step and validation rule['required'] == False
  then variable's values above are None 

  """
```


#### @Bot.arguments
Decorator checks command line arguments and validates the arguments according to provided rules.
NOTE: arguments can't be optional!
If user puts less arguments count than it shows message like:

```
Enter command: add-phone Igor
Invalid number of arguments, expected: <name>, <phone>
```

Basically, that works the same way as questions for wizard mode:

```
@Bot.command('add-phone')
@Bot.description('used to add a phone to contact')
@Bot.questions([
    {
        # arument name in the error message, if user doesn't put in command args
        'name': 'name', 
                
        # class which validates the data.
        # it equals to str by default
        # if class throws ValidationValueException, exception message is shown to the user 
        'type': str
    },
    {
        'name': 'phone',
        'type': Phone
    }
])
def add_contact(ctx: Context, args):
  """
    As that funciton uses 2 arguments,
    in the args array there are:
  """

  name, phone, birthday, email = args
  """
  name = instance of str class
  phone - instance of Phone class

  """
```