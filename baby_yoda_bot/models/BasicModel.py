import pickle


class BasicModel:
    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self.data, file)

    def read_from_file(self):
        try:
            with open(self.filename, "rb") as file:
                self.data = pickle.load(file)
            return self.data
        except (OSError, IOError) as e:
            pass

    def show(self):
        if len(self.data) == 0:
            print("Address Book is empty")
        for record in self.data.values():
            print(record)
