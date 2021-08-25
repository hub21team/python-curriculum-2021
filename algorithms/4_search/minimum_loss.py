"""
Lauren has a chart of distinct projected prices for a house over the next several years. She must buy the house in one year and sell it in another, and she must do so at a loss. She wants to minimize her financial loss.

Example:
prices = [20, 15, 8, 2, 12]
Her minimum loss is incurred by purchasing in year 2 at price[1]=15 and reselling in year[5] at price[4]=12. Return 15-12=3.

Function Description
Complete the minimum_loss function, which takes the following parameters:
- int prices: home prices in each year

Returns
- int: the minimum loss possible

Input Format

The first line contains an integer n, the number of years of house data.
The second line contains n space-separated long integers that describe each price[i].

Constraints:
- 2 <= n <= 2x10^5
- 1 <= prices[i] <= 1e16
- All prices are distinct.
- A valid answer exists.

Sample Output:
minimum_loss/input1.txt
Test Case 1, the minimum loss is 2
minimum_loss/input2.txt
Test Case 2, the minimum loss is 2
minimum_loss/input5.txt
Test Case 3, the minimum loss is 99727
"""
def minimum_loss(prices):
    prices_sorted = sorted(enumerate(prices), key=lambda p: p[1])
    prices = [p[1] for p in prices_sorted]
    min_loss = 1e9
    for i in range(len(prices)-1):
        j = i+1
        # ie. i'th price happened before j'th
        if prices_sorted[i][0] < prices_sorted[j][0]:
            loss = prices[i] - prices[j]
        else:
            loss = prices[j] - prices[i]
        if 0 < loss < min_loss:
            min_loss = loss
    return min_loss


def naive_minimum_loss(prices):
    # Write your code here
    min_loss = 1e9
    for i in range(len(prices)-1):
        for j in range(i+1, len(prices)):
            loss = prices[i] - prices[j]
            if 0 < loss < min_loss:
                min_loss = loss
    return min_loss


def minimum_loss_exercise():
    # first parse inputs
    import os
    input_dir = os.path.join(os.path.abspath(
        os.path.dirname(__file__)), "input", "minimum_loss")
    test_case = 1
    for f in os.listdir(input_dir):
        input_file = os.path.join(input_dir, f)
        print(input_file)
        with open(input_file, "r") as fl:
            line_num = 0
            for line in fl:
                if line_num == 0:
                    n = int(line)
                else:
                    l = line.split()
                    prices = [int(i) for i in l]
                line_num += 1
            min_loss = naive_minimum_loss(prices)
            print(f"Test Case {test_case}, the minimum loss is {min_loss}")
        test_case += 1


minimum_loss_exercise()
