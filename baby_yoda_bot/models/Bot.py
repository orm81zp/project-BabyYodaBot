from .BotLogic import BotLogic


class Bot(BotLogic):
    def start(self):
        while True:
            try:
                cmd, args = self.requestCommand()

                # Todo parcing from dictinary
                if cmd:
                    if cmd == "add-contact":
                        self.add_contact(args)
                    elif cmd == "all-contacts":
                        self.show_all()
                    elif cmd == "help":
                        self.show_help()
                    elif cmd in ["exit", "close"]:
                        print("Bye!")
                        break
                    else:
                        print('Invalid command. Type "help" to see a hint.')
                else:
                    print("Please tell me something :(")
            except Exception as err:
                print(err)
