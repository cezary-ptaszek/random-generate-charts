class Chart:
    def __init__(self, data, destination):
        self.data = data
        self.destination = destination

    def plotAndSave(self):
        print(self.data, self.destination)
