from math import sqrt
def euclidean_dist(x, y):
    for i, j in x, y:
        distance  += (j - i)**2
    distance = sqrt(distance)
    return distance

def manhattan_dist(x, y):
    distance = 0
    for i, j in x, y:
        distance  += abs(j - i)
    return distance

def jaccard_dist(x, y):
    union = set(x + y)
    print(union)
    intersection =[]
    for elem in x:
        if elem in y:
            intersection.append(elem)
    print(intersection)
    distance = len(intersection)/len(union)
    return distance

def cosine_sim(x, y):
    raise NotImplementedError()

# Feel free to add more
# print(euclidean_dist((2,4),(4,8)))
# print(manhattan_dist((2,4),(4,8)))

x = (1,2,3,4)
y = (4,5,6)

print(jaccard_dist(x,y))