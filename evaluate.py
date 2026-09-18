from predict import estimate_price, load_theta
from train import load_data


def mean_squared_error(mileages, prices, theta0, theta1):
    m = len(mileages)
    squared_errors = [
        (estimate_price(mileages[i], theta0, theta1) - prices[i]) ** 2
        for i in range(m)
    ]
    return sum(squared_errors) / m


def r2_score(mileages, prices, theta0, theta1):
    m = len(prices)
    mean_price = sum(prices) / m

    residual_sum_of_squares = sum(
        (prices[i] - estimate_price(mileages[i], theta0, theta1)) ** 2
        for i in range(m)
    )
    total_sum_of_squares = sum((price - mean_price) ** 2 for price in prices)

    return 1 - residual_sum_of_squares / total_sum_of_squares


def main():
    mileages, prices = load_data("data.csv")
    theta0, theta1 = load_theta("theta.txt")

    rmse = mean_squared_error(mileages, prices, theta0, theta1) ** 0.5
    r2 = r2_score(mileages, prices, theta0, theta1)

    print(f"RMSE: {rmse}")
    print(f"R2:   {r2}")


if __name__ == "__main__":
    main()
