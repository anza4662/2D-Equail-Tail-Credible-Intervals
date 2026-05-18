import numpy as np
import pandas as pd
from matplotlib import pyplot as plt



#Gaussian
def gaussian_data(n=10000):
    mean = [0, 0]

    covariance = [
        [3, 2],
        [2, 2]
    ]

    data = np.random.multivariate_normal(mean, covariance, n)

    return pd.DataFrame(data, columns=["x1", "x2"])


# Two-cluster distribution
def bimodal_data(n=10000):

    n1 = n // 2
    n2 = n - n1

    cluster1 = np.random.multivariate_normal(
        [-4, -4],
        [[1, 0.3],
         [0.3, 1]],
        n1
    )

    cluster2 = np.random.multivariate_normal(
        [4, 4],
        [[1, -0.5],
         [-0.5, 1]],
        n2
    )

    data = np.vstack([cluster1, cluster2])

    return pd.DataFrame(data, columns=["x1", "x2"])


# Uniform square
def square_data(n=10000):

    x = np.random.uniform(-5, 5, n)
    y = np.random.uniform(-5, 5, n)

    return pd.DataFrame({
        "x1": x,
        "x2": y
    })

if __name__ == "__main__":
    # data = gaussian_data()
    # data = bimodal_data()
    data = square_data()

    data.to_csv("posterior_mock_data.csv", index=False)

    plt.figure(figsize=(6, 6))
    plt.scatter(data["x1"], data["x2"], s=5)
    plt.title("Generated Test Dataset")
    plt.show()