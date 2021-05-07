n = int(input())

positives = []
negatives = []
count_positives = 0
sum_of_negatives = 0

for _ in range(n):
    num = int(input())
    if num >= 0:
        positives.append(num)
        count_positives += 1
    negatives.append(num)
    if num < 0:
        sum_of_negatives += num


print(f"Count of positives: {count_positives}. Sum of negatives: {sum_of_negatives}")

