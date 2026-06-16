class Memory:
    def __init__(self):
        self.memories = []

    def add(self, text):
        self.memories.append(text)

    def get_all(self):
        return self.memories