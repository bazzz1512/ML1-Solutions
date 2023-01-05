import numpy as np
import matplotlib.pyplot as plt
import prtools as pr
from sklearn import cluster, model_selection
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
        new_boomerangs = +pr.boomerangs(100)
        print(new_boomerangs)

        plt.figure()
        plt.title("Boomerangs Feature 2-3")
        plt.scatter(new_boomerangs[:, 1], new_boomerangs[:, 2])

        plt.figure()
        plt.title("Boomerangs Feature 1-2")
        plt.scatter(new_boomerangs[:, 0], new_boomerangs[:, 1])
        plt.show()

    def exc1_10(self):
        new_boomerangs = +pr.boomerangs(100)
        print(new_boomerangs)

        plt.figure()
        plt.title("Boomerangs Feature 2-3")
        plt.scatter(new_boomerangs[:, 1], new_boomerangs[:, 2])

        plt.figure()
        plt.title("Boomerangs Feature 1-2")
        plt.scatter(new_boomerangs[:, 0], new_boomerangs[:, 1])
        plt.show()

        # Do nearest mean clustering on boomerangs and plot the results, do this with scikit-learn

        # Create a KMeans object
        kmeans = cluster.KMeans(n_clusters=2)

        # Split into training and test data
        train_data, test_data = model_selection.train_test_split(new_boomerangs, test_size=0.2)

        # Fit the model
        kmeans.fit(train_data)

        # Predict the labels
        labels = kmeans.predict(test_data)

        # Plot the results
        plt.figure()
        plt.title("Boomerangs Feature 2-3")
        plt.scatter(new_boomerangs[:, 1], new_boomerangs[:, 2])
        plt.scatter(test_data[:, 1], test_data[:, 2], c=labels)
        plt.show()









