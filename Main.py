import matplotlib.pyplot as plt
import numpy.random as npr
import pandas as pd

films = pd.read_csv("res/films.csv")
deaths = pd.read_csv("res/zgony.csv")
iris = pd.read_csv("res/iris.csv")

COUNT = 10
TRAIN_DESTINATION = "train/"
DEV_DESTINATION = "dev-0/"
TEST_DESTINATION = "test-A/"


def linear(size):
    return npr.randint(50, size=size)


def square():
    return npr.randint(2, 10)**npr.randint(2, 12)


def checkFunction(num, size):
    if num == 1:
        a = linear(size)
    else:
        a = square()
    return a


def randomNumbers():
    size = npr.randint(2, 12)
    num = npr.randint(1, 3)
    print("Rodzaj funkcji: " + str(num))
    x = checkFunction(num, size)
    y = checkFunction(num, size)
    return x, y


def randomColor():
    r = npr.random()
    b = npr.random()
    g = npr.random()
    return r, g, b


def savingImage(destination):
    for i in range(COUNT):
        print("Wykres: " + str(i))
        for j in range(npr.randint(0, 10)):
            print("Ilość kresek: " + str(j))
            plt.plot(randomNumbers(), color=randomColor())
            df = pd.DataFrame(randomNumbers())
            df.to_csv(destination + 'expected' + str(i) + '.tsv', sep='\t')
        plt.savefig(destination + 'in' + str(i) + '.png')


if __name__ == "__main__":
    savingImage(TRAIN_DESTINATION)
    savingImage(DEV_DESTINATION)
    savingImage(TEST_DESTINATION)
