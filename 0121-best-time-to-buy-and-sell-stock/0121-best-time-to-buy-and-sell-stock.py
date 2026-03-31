class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_buy_price = prices[0]

        max_profit = 0


        for i in range(1, len(prices)):
            current_price = prices[i]


            if current_price < min_buy_price:
                min_buy_price = current_price
            
            elif current_price - min_buy_price > max_profit:
                max_profit = current_price - min_buy_price
                
        return max_profit