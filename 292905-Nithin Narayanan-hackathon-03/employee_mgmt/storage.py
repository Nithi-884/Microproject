import pickle

class Storage:
    def __init__(self, filename):
        self.filename = filename

# open file and dumb
    def save(self, data):
        with open(self.filename, 'wb') as file:
            pickle.dump(data, file)
# Loads and return data
    def load(self):
        try:
            with open(self.filename, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, EOFError, pickle.UnpicklingError):
            return []
