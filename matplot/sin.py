import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    x = np.linspace(0, 2 * np.pi, 200)
    y = np.sin(x)

    fig, ax = plt.subplots()
    ax.plot(x, y)
    plt.show()