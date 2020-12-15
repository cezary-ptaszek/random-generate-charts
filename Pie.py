import matplotlib.pyplot as plt


def plotAndSave(data, destination):
    a = data.value_counts()
    species = a.index
    count = a.values
    colors = ['lightblue', 'lightgreen', 'gold']
    explode = (0, 0.2, 0)
    plt.pie(count, labels=species, shadow=True,
            colors=colors, explode=explode, autopct='%1.1f%%')
    plt.xlabel('species')
    plt.axis('equal')
    plt.savefig(destination)
