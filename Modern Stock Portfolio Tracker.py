from typing import Dict

class PortfolioTracker:
    def __init__(self):
        # Hardcoded dictionary for stock prices
        self.market_prices: Dict[str, float] = {
            "AAPL": 180.0, "TSLA": 250.0, "GOOGL": 140.0, "MSFT": 400.0
        }
        self.portfolio: Dict[str, int] = {}

    def add_stock(self, ticker: str, quantity: int):
        if ticker in self.market_prices:
            self.portfolio[ticker] = self.portfolio.get(ticker, 0) + quantity
            print(f"Successfully added {quantity} shares of {ticker}.")
        else:
            print(f"Error: '{ticker}' is not in our database.")

    def generate_report(self):
        total_value = 0.0
        report_lines = ["\n--- Modern Portfolio Summary ---"]
        
        for ticker, qty in self.portfolio.items():
            price = self.market_prices[ticker]
            value = price * qty
            total_value += value
            report_lines.append(f"{ticker}: {qty} shares @ ${price:.2f} = ${value:.2f}")
        
        report_lines.append(f"\nTotal Investment Value: ${total_value:.2f}")
        report_content = "\n".join(report_lines)
        
        print(report_content)
        
        # Save the result in a .txt file
        with open("portfolio_report.txt", "w") as file:
            file.write(report_content)
        print("\nReport saved successfully to 'portfolio_report.txt'.")

if __name__ == "__main__":
    tracker = PortfolioTracker()
    print("Available Stocks:", ", ".join(tracker.market_prices.keys()))
    
    while True:
        ticker = input("\nEnter stock ticker (or 'done' to exit): ").strip().upper()
        if ticker == "DONE":
            break
            
        try:
            qty = int(input(f"Enter quantity for {ticker}: "))
            if qty > 0:
                tracker.add_stock(ticker, qty)
            else:
                print("Quantity must be a positive number.")
        except ValueError:
            print("Invalid format. Please enter numbers only for quantity.")
            
    if tracker.portfolio:
        tracker.generate_report()