
purchase_amount = float(input())


loyalty_points = int(purchase_amount // 10)


start_index = int(input())


boxes = []
try:
    while True:
        box = input()
        boxes.append(box)
except EOFError:
    pass


print(loyalty_points)


for i in range(start_index, len(boxes)):
    print(boxes[i])
