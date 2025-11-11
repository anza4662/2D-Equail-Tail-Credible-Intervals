import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def two_var_et_ci(data, alpha, nr_of_axes):
    axes = np.arange(0, np.pi, np.pi/nr_of_axes)
    new_data = np.array(data)

    while len(new_data) > (1-alpha) * len(data):

        axis = np.random.choice(axes)

        rotation_matrix = np.array([[np.cos(axis), -np.sin(axis)],
                                    [np.sin(axis), np.cos(axis)]])

        rotated_new_data = np.transpose(np.matmul(rotation_matrix, np.transpose(new_data)))
        sorted_rotated_new_data = np.reshape(sorted(rotated_new_data, key = lambda x: x[0]), [len(rotated_new_data), 2])
        sorted_rotated_new_data = np.delete(sorted_rotated_new_data, (0,-1), axis = 0)

        inverse_rotation_matrix = np.array([[-np.cos(axis), np.sin(axis)],
                                            [-np.sin(axis), -np.cos(axis)]])
        new_data = np.transpose(np.matmul(inverse_rotation_matrix, np.transpose(sorted_rotated_new_data)))

    return pd.DataFrame(data = new_data, columns = ["x1", "x2"])


def main():
    data = pd.read_csv('posterior_data.csv')

    plt.plot(data["ext_pois.N"], data["ext_pois.theta"], "bo")
    plt.title('Full posterior')
    plt.show()

    result = two_var_et_ci(data, alpha = 0.5, nr_of_axes = 2)

    plt.plot(result["x1"], result["x2"], "bo")
    plt.title('Equal-tail credible interval')
    plt.show()


if __name__ == '__main__':
    main()
