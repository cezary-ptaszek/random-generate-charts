import matplotlib.pyplot as plt
import numpy.random as npr
import numpy as np
import pandas as pd
import random as r

films = pd.read_csv("res/films.csv")
deaths = pd.read_csv("res/zgony.csv")
iris = pd.read_csv("res/iris.csv")

COUNT = 10
TRAIN_DESTINATION = "train/"
DEV_DESTINATION = "dev-0/"
TEST_DESTINATION = "test-A/"


def randomColor():
    r = npr.random()
    b = npr.random()
    g = npr.random()
    return r, g, b


def savingImage(destination):
    for i in range(COUNT):
        print("Wykres: " + str(i))
        # ------------------------------------------------------------------
        # wykres liniowy
        for j in range(npr.randint(0, 6)):
            size = npr.randint(20, 60)
            ts = pd.Series(npr.randn(size), index=np.arange(size))
            ts = ts.cumsum()
            ts.plot(color=randomColor())
            ts.to_csv(destination + 'expected' + str(i) + '.tsv', sep='\t')
        if bool(r.getrandbits(1) == 1):
            plt.grid(linewidth=0.5, color='#000000', linestyle='-')
        plt.savefig(destination + 'in' + str(i) + '.png')
        plt.close()
        # ------------------------------------------------------------------

        # wykres slupkowy


if __name__ == "__main__":
    savingImage(TRAIN_DESTINATION)
    savingImage(DEV_DESTINATION)
    savingImage(TEST_DESTINATION)
