import sys

import matplotlib.pyplot as plt

from predict import estimate_price, load_theta
from train import load_data


def main():
    mileages, prices = load_data("data.csv")

    try:
        theta0, theta1 = load_theta("theta.txt")
    except ValueError as e:
        print(f"エラー: {e}")
        sys.exit(1)

    line_x = [min(mileages), max(mileages)]
    line_y = [estimate_price(x, theta0, theta1) for x in line_x]

    plt.scatter(mileages, prices, label="data")
    plt.plot(line_x, line_y, color="red", label="regression line")
    plt.xlabel("mileage (km)")
    plt.ylabel("price")
    plt.title("Car price vs mileage")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
