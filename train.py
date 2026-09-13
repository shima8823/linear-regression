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

    for iteration in range(iterations):
        errors = [
            estimate_price(mileages[i], theta0, theta1) - prices[i]
            for i in range(m)
        ]
        tmp_theta0 = learning_rate * (1 / m) * sum(errors)
        tmp_theta1 = learning_rate * (1 / m) * sum(
            errors[i] * mileages[i] for i in range(m)
        )
        theta0 -= tmp_theta0
        theta1 -= tmp_theta1

        if iteration % 100 == 0:
            print(f"iteration {iteration}: theta0={theta0}, theta1={theta1}")

    return theta0, theta1


def standardize(values):
    m = len(values)
    mean = sum(values) / m
    variance = sum((v - mean) ** 2 for v in values) / m
    std = variance**0.5
    scaled = [(v - mean) / std for v in values]
    return scaled, mean, std


def unscale_theta(theta0_scaled, theta1_scaled, mean, std):
    theta1 = theta1_scaled / std
    theta0 = theta0_scaled - theta1_scaled * mean / std
    return theta0, theta1


def main():
    mileages, prices = load_data("data.csv")

    mileages_scaled, mileage_mean, mileage_std = standardize(mileages)

    theta0_scaled, theta1_scaled = train(
        mileages_scaled, prices, learning_rate=0.1, iterations=1000
    )
    print(f"scaled theta: theta0={theta0_scaled}, theta1={theta1_scaled}")

    theta0, theta1 = unscale_theta(
        theta0_scaled, theta1_scaled, mileage_mean, mileage_std
    )
    print(f"final: theta0={theta0}, theta1={theta1}")

    with open("theta.txt", "w") as f:
        f.write(f"{theta0},{theta1}")


if __name__ == "__main__":
    main()
