# Print Positive Negative Integer
def plusMinus(arr):
    # Write your code here
    positive_ratio, negative_ratio, zero_ratio = (format(len([x for x in arr if x > 0]) / len(arr), ".6f"),format(len([x for x in arr if x < 0]) / len(arr), ".6f"),format(len([x for x in arr if x == 0]) / len(arr), ".6f"),)
    print(positive_ratio)
    print(negative_ratio)
    print(zero_ratio)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)