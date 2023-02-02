# number of balls
number_of_balls = 5
# number of boxes
number_of_boxes = 3

# partitions
partitions = []

def make_partitions(n, m, partition: list):
    if m == 1:
        partition.append(n)
        partitions.append(partition)

        return
    else:
        for i in range(1,n):
            
            make_partitions(n - i, m -1, partition + [i])


make_partitions(number_of_balls, number_of_boxes, [])

print(partitions)