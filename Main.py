import matplotlib.pyplot as plt
import numpy.random as npr
import pandas as pd

films = pd.read_csv("films.csv")
deaths = pd.read_csv("zgony.csv", encoding="utf-8")
iris = pd.read_csv("iris.csv")
register = pd.read_csv("rejestr.csv", encoding="utf-8")

COUNT = 10
DESTINATION = "dest/"


def randomNumbers():
    size = npr.randint(0, 100)
    x = npr.randint(100, size=size)
    y = npr.randint(100, size=size)
    return x, y


def randomColor():
    r = npr.random()
    b = npr.random()
    g = npr.random()
    return r, g, b


def savingImage():
    for i in range(COUNT):
        data = randomNumbers()
        for j in range(npr.randint(0, 5)):
            plt.plot(data, color=randomColor())
        name = DESTINATION + "char" + str(i) + ".png"
        plt.savefig(name)
        df = pd.DataFrame(data)
        df.to_csv(name)


if __name__ == "__main__":
    savingImage()
