stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 320,
    "AMZN": 140
}

total_investment = 0

print("Welcome to Stock Portfolio Tracker")

while True:
    stock_name = input("Enter Stock Name (AAPL, TSLA, GOOGL, MSFT, AMZN): ").upper()

    if stock_name in stock_prices:
        quantity = int(input("Enter Quantity: "))
        investment = stock_prices[stock_name] * quantity
        total_investment += investment
        print("Investment for", stock_name, "=", investment)
    else:
        print("Stock not found.")

    choice = input("Do you want to add another stock? (yes/no): ").lower()

    if choice != "yes":
        break

print("\nTotal Investment Value =", total_investment)

file = open("investment_result.txt", "w")
file.write("Total Investment Value = " + str(total_investment))
file.close()

print("Result saved in investment_result.txt")
