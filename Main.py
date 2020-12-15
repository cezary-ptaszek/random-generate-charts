import matplotlib.pyplot as plt
import numpy.random as npr
import numpy as np
import pandas as pd
import random as r

films = pd.read_csv("res/films.csv")
deaths = pd.read_csv("res/zgony.csv")
iris = pd.read_csv("res/iris.csv")

COUNT_LINEAR_SCATTER = 0
COUNT_BAR_HIST_BOX_PIE = 0
COUNT_HIST = 0

TRAIN_DESTINATION = "train/"
DEV_DESTINATION = "dev-0/"
TEST_DESTINATION = "test-A/"


def randomColor():
    r1 = npr.random()
    b1 = npr.random()
    g1 = npr.random()
    return r1, g1, b1


def savingImage(destination):
    index_all = 1
    # ------------------------------------------------------------------
    for i in range(COUNT_LINEAR_SCATTER):
        print("Wykres liniowy: " + str(i))
        # wykres liniowy
        for j in range(npr.randint(0, 6)):
            size = npr.randint(20, 60)
            ts = pd.Series(npr.randn(size), index=np.arange(size))
            ts = ts.cumsum()
            ts.plot(color=randomColor())
            ts.to_csv(destination + 'expected' + str(index_all) + '.tsv', sep='\t')
        if bool(r.getrandbits(1) == 1):
            plt.grid(linewidth=0.5, color='#000000', linestyle='-')
        plt.savefig(destination + 'in' + str(index_all) + '.png')
        plt.close()
        index_all += 1
    # ------------------------------------------------------------------

    for i in range(COUNT_BAR_HIST_BOX_PIE):
        # wykres slupkowy 1
        print("Wykres slupkowy: " + str(i))
        df2 = pd.DataFrame(npr.rand(10, 1), columns=['a'])
        df2.plot.bar()
        if bool(r.getrandbits(1) == 1):
            plt.grid(linewidth=0.5, color='#000000', linestyle='-')
        if bool(r.getrandbits(1) == 1):
            df2.plot.bar(stacked=True)
        if bool(r.getrandbits(1) == 1):
            df2.plot.barh(stacked=True)
        df2.to_csv(destination + 'expected' + str(index_all) + '.tsv', sep='\t')
        plt.savefig(destination + 'in' + str(index_all) + '.png')
        plt.close()
        index_all += 1

    for i in range(COUNT_BAR_HIST_BOX_PIE):
        # wykres slupkowy 2
        print("Wykres slupkowy: " + str(i))
        df2 = pd.DataFrame(npr.rand(10, 2), columns=['a', 'b'])
        df2.plot.bar()
        if bool(r.getrandbits(1) == 1):
            plt.grid(linewidth=0.5, color='#000000', linestyle='-')
        if bool(r.getrandbits(1) == 1):
            df2.plot.bar(stacked=True)
        if bool(r.getrandbits(1) == 1):
            df2.plot.barh(stacked=True)
        df2.to_csv(destination + 'expected' + str(index_all) + '.tsv', sep='\t')
        plt.savefig(destination + 'in' + str(index_all) + '.png')
        plt.close()
        index_all += 1

    for i in range(COUNT_BAR_HIST_BOX_PIE):
        # wykres slupkowy 3
        print("Wykres slupkowy: " + str(i))
        df2 = pd.DataFrame(npr.rand(10, 3), columns=['a', 'b', 'c'])
        df2.plot.bar()
        if bool(r.getrandbits(1) == 1):
            plt.grid(linewidth=0.5, color='#000000', linestyle='-')
        if bool(r.getrandbits(1) == 1):
            df2.plot.bar(stacked=True)
        if bool(r.getrandbits(1) == 1):
            df2.plot.barh(stacked=True)
        df2.to_csv(destination + 'expected' + str(index_all) + '.tsv', sep='\t')
        plt.savefig(destination + 'in' + str(index_all) + '.png')
        plt.close()
        index_all += 1
    # ------------------------------------------------------------------
    for i in range(COUNT_BAR_HIST_BOX_PIE):
        print("Histogram: " + str(i))
        df4 = pd.DataFrame({'a': npr.randn(1000) + 1, 'b': npr.randn(1000),
                            'c': npr.randn(1000) - 1}, columns=['a', 'b', 'c'])
        plt.figure()
        if bool(r.getrandbits(1) == 1):
            df4.plot.hist(alpha=0.5)
        if bool(r.getrandbits(1) == 1):
            df4.plot.hist(stacked=True, bins=20)
        if bool(r.getrandbits(1) == 1):
            plt.grid(linewidth=0.5, color='#000000', linestyle='-')
        df4.to_csv(destination + 'expected' + str(index_all) + '.tsv', sep='\t')
        plt.savefig(destination + 'in' + str(index_all) + '.png')
        plt.close()
        index_all += 1

    for i in range(COUNT_BAR_HIST_BOX_PIE):
        print("Histogram: " + str(i))
        df4 = pd.DataFrame({'a': npr.randn(1000) + 1, 'b': npr.randn(1000)}, columns=['a', 'b'])
        plt.figure()
        if bool(r.getrandbits(1) == 1):
            df4.plot.hist(alpha=0.5)
        if bool(r.getrandbits(1) == 1):
            df4.plot.hist(stacked=True, bins=20)
        if bool(r.getrandbits(1) == 1):
            plt.grid(linewidth=0.5, color='#000000', linestyle='-')
        df4.to_csv(destination + 'expected' + str(index_all) + '.tsv', sep='\t')
        plt.savefig(destination + 'in' + str(index_all) + '.png')
        plt.close()
        index_all += 1

    for i in range(COUNT_BAR_HIST_BOX_PIE):
        print("Histogram: " + str(i))
        df4 = pd.DataFrame({'a': npr.randn(1000) + 1}, columns=['a'])
        plt.figure()
        if bool(r.getrandbits(1) == 1):
            df4.plot.hist(alpha=0.5)
        if bool(r.getrandbits(1) == 1):
            df4.plot.hist(stacked=True, bins=20)
        if bool(r.getrandbits(1) == 1):
            plt.grid(linewidth=0.5, color='#000000', linestyle='-')
        if bool(r.getrandbits(1) == 1):
            df4['a'].plot.hist(orientation='horizontal', cumulative=True)
        df4.to_csv(destination + 'expected' + str(index_all) + '.tsv', sep='\t')
        plt.savefig(destination + 'in' + str(index_all) + '.png')
        plt.close()
        index_all += 1
    # ------------------------------------------------------------------

    for i in range(COUNT_BAR_HIST_BOX_PIE):
        print("Wykres boxowy: " + str(i))
        df = pd.DataFrame(np.random.rand(10, 5), columns=['A', 'B', 'C', 'D', 'E'])
        df.plot.box(color=randomColor(), sym='r+')
        if bool(r.getrandbits(1) == 1):
            df.plot.box(vert=False, positions=[1, 4, 5, 6, 8])
        if bool(r.getrandbits(1) == 1):
            df.plot.box(vert=False, positions=[2, 3, 5, 7, 8])
        if bool(r.getrandbits(1) == 1):
            df.plot.box(vert=False, positions=[1, 2, 6, 7, 8])
        df.to_csv(destination + 'expected' + str(index_all) + '.tsv', sep='\t')
        plt.savefig(destination + 'in' + str(index_all) + '.png')
        plt.close()
        index_all += 1

    for i in range(COUNT_BAR_HIST_BOX_PIE):
        print("Wykres boxowy: " + str(i))
        df = pd.DataFrame(np.random.rand(10, 3), columns=['A', 'B', 'C'])
        df.plot.box(color=randomColor(), sym='r+')
        if bool(r.getrandbits(1) == 1):
            df.plot.box(vert=False, positions=[1, 2, 5])
        if bool(r.getrandbits(1) == 1):
            df.plot.box(vert=False, positions=[1, 3, 4])
        if bool(r.getrandbits(1) == 1):
            df.plot.box(vert=False, positions=[2, 4, 5])
        df.to_csv(destination + 'expected' + str(index_all) + '.tsv', sep='\t')
        plt.savefig(destination + 'in' + str(index_all) + '.png')
        plt.close()
        index_all += 1

    for i in range(COUNT_BAR_HIST_BOX_PIE):
        print("Wykres boxowy: " + str(i))
        df = pd.DataFrame(npr.rand(10, 2), columns=['A', 'B'])
        df.plot.box(color=randomColor(), sym='r+')
        if bool(r.getrandbits(1) == 1):
            df.plot.box(vert=False, positions=[1, 3])
        if bool(r.getrandbits(1) == 1):
            df.plot.box(vert=False, positions=[1, 2])
        df.to_csv(destination + 'expected' + str(index_all) + '.tsv', sep='\t')
        plt.savefig(destination + 'in' + str(index_all) + '.png')
        plt.close()
        index_all += 1
    # ------------------------------------------------------------------
    for i in range(COUNT_LINEAR_SCATTER):
        print("Wykres kropkowy: " + str(i))
        df = pd.DataFrame(np.random.rand(50, 4), columns=['a', 'b', 'c', 'd'])
        df.plot.scatter(x='a', y='b')
        if bool(r.getrandbits(1) == 1):
            ax = df.plot.scatter(x='a', y='b', color=randomColor(), label='Group 1')
            df.plot.scatter(x='c', y='d', color=randomColor(), label='Group 2', ax=ax)
        if bool(r.getrandbits(1) == 1):
            df.plot.scatter(x='a', y='b', c='c', s=50)
        df.to_csv(destination + 'expected' + str(index_all) + '.tsv', sep='\t')
        plt.savefig(destination + 'in' + str(index_all) + '.png')
        plt.close()
        index_all += 1
    # ------------------------------------------------------------------
    for i in range(COUNT_BAR_HIST_BOX_PIE):
        print("Wykres kołowy: " + str(i))
        s = pd.Series(3 * np.random.rand(4), index=['a', 'b', 'c', 'd'], name='series')
        s.plot.pie(figsize=(6, 6), colors=[randomColor(), randomColor(), randomColor(), randomColor()])
        if bool(r.getrandbits(1) == 1):
            s.plot.pie(labels=['A1', 'A2', 'A3', 'A4'], colors=[randomColor(), randomColor(), randomColor(),
                                                                randomColor()],
                       autopct='%.2f', fontsize=14, figsize=(6, 6))
        s.to_csv(destination + 'expected' + str(index_all) + '.tsv', sep='\t')
        plt.savefig(destination + 'in' + str(index_all) + '.png')
        plt.close()
        index_all += 1

    for i in range(COUNT_BAR_HIST_BOX_PIE):
        print("Wykres kołowy: " + str(i))
        s = pd.Series(3 * np.random.rand(4), index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], name='series')
        s.plot.pie(figsize=(6, 6), colors=[randomColor(), randomColor(), randomColor(), randomColor()])
        if bool(r.getrandbits(1) == 1):
            s.plot.pie(labels=['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8'], colors=[randomColor(), randomColor(),
                                                                                        randomColor(), randomColor(),
                                                                                        randomColor(), randomColor(),
                                                                                        randomColor(), randomColor()],
                       autopct='%.2f', fontsize=14, figsize=(6, 6))
        s.to_csv(destination + 'expected' + str(index_all) + '.tsv', sep='\t')
        plt.savefig(destination + 'in' + str(index_all) + '.png')
        plt.close()
        index_all += 1


if __name__ == "__main__":
    COUNT_LINEAR_SCATTER = 1000
    COUNT_BAR_HIST_BOX_PIE = 200
    print("Gen train: ")
    savingImage(TRAIN_DESTINATION)
    COUNT_LINEAR_SCATTER = 200
    COUNT_BAR_HIST_BOX_PIE = 50
    print("Gen dev: ")
    savingImage(DEV_DESTINATION)
    print("Gen test: ")
    savingImage(TEST_DESTINATION)
