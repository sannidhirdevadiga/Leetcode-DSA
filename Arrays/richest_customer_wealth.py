class Solution:
    def maximumWealth(self, accounts):
        max_wealth = 0

        for customer in accounts:
            total = 0

            for money in customer:
                total += money

            if total > max_wealth:
                max_wealth = total

        return max_wealth


accounts = [[1, 2, 3], [3, 2, 1]]

solution = Solution()
print(solution.maximumWealth(accounts))