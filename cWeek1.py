import numpy as np
import matplotlib.pyplot as plt


class Week1:
    def __init__(self):
        self.name = "Week1"
        self.description = "Week1"

    def exc1_6(self):
        data = np.random.random((10, 3))

        print(f"Data:\n{data}")

        mean = data.mean(axis=1)
        print(f"Mean:\n{mean}")

        deviation = data.std()

        print(f"Standard deviation:\n{deviation}")
        # .mean() computes mean of all items
        # .mean(axis=0) computes mean of each column
        # .mean(axis=1) computes mean of each row

    def exc1_7(self):
        data = np.random.random((10, 3))

        plt.scatter(data[:, 0], data[:, 1])
        plt.show()

        # Can't find any structure, because the data is random

    def exc1_8(self):
        data = np.random.random((10, 3))
        labels = np.ones((10, 1))
        labels[5:] = 2
        data_with_labels = np.concatenate((data, labels), axis=1)
        print(f"Data with labels:\n{data_with_labels}")

    def exc1_9(self):
        pass




