class CryptocurrencyTradingBot:
    """
    Cryptocurrency Trading Bot 🤖💰
    Calculates the maximum possible profit from a given list of cryptocurrency prices.
    """

    def __init__(self, prices, budget):
        """
        Constructor for initializing the bot.

        :param prices: List of cryptocurrency prices over time.
        :param budget: Available budget (not directly used in profit calculation).
        """
        self.prices = prices
        self.budget = budget

    def calculate_profit(self):
        """
        Calculates the maximum profit by finding the best buy and sell times.

        :return: Tuple (max_profit, buy_index, sell_index)
                 If no profit is possible, returns (0, 0, 0).
        """

        # Initialize variables
        max_profit = 0
        buy_index = 0
        sell_index = 0

        # Iterate through all pairs of (buy, sell) prices
        for i in range(len(self.prices)):
            for j in range(i + 1, len(self.prices)):
                # Calculate profit if bought at i and sold at j
                profit = self.prices[j] - self.prices[i]

                # Update max profit if this pair is better
                if profit > max_profit:
                    max_profit = profit
                    buy_index = i
                    sell_index = j

        # Return result — only if profit exists
        if max_profit > 0:
            return (max_profit, buy_index, sell_index)
        else:
            return (0, 0, 0)
