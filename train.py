import csv

from predict import estimate_price


def load_data(path):
    mileages, prices = [], []
    with open(path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            mileages.append(float(row["km"]))
            prices.append(float(row["price"]))
    return mileages, prices


def train(mileages, prices, learning_rate, iterations):
    theta0, theta1 = 0.0, 0.0
    m = len(mileages)

    for i in range(iterations):
        errors = [
            estimate_price(mileages[j], theta0, theta1) - prices[j]
            for j in range(m)
        ]
        tmp_theta0 = learning_rate * (1 / m) * sum(errors)
        tmp_theta1 = learning_rate * (1 / m) * sum(
            errors[j] * mileages[j] for j in range(m)
        )
        theta0 -= tmp_theta0
        theta1 -= tmp_theta1

        if i % 100 == 0:
            print(f"iteration {i}: theta0={theta0}, theta1={theta1}")

    return theta0, theta1


def main():
    mileages, prices = load_data("data.csv")
    theta0, theta1 = train(mileages, prices, learning_rate=0.1, iterations=1000)
    print(f"final: theta0={theta0}, theta1={theta1}")


if __name__ == "__main__":
    main()
