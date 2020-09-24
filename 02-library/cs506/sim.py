from math import sqrt

# Andrew Whittum contributions to CS506-Fall2020 code base

def euclidean_dist(x, y):

    # input checks
    if check_for_null(x, y) or check_for_diff_length(x, y):
        return ValueError

    # take the square root of sum of distances squared for ith value in each vector
    distance = 0
    for i, j in zip(x, y):
        distance += (j - i)**2
    distance = sqrt(distance)
    
    return distance


def manhattan_dist(x, y):

    # run checks
    if check_for_null(x, y) or check_for_diff_length(x, y):
        return ValueError

    # calculate sum of absolute value of the difference for ith pair of values
    distance = 0
    for i, j in zip(x, y):
        distance += abs(j - i)
        
    return distance

def jaccard_dist(x, y):

    # run checks
    if check_for_null(x, y) or check_for_diff_length(x, y):
        return ValueError

    # generate the union of the two vectors w/ no repeats
    union = list(set(x + y))

    # generate the intersection of the two vectors
    intersection =[]
    for elem in x:
        if elem in y:
            if elem in intersection:
                continue
            else:
                intersection.append(elem)

    # divide number of values in both by total number of unique values between the two vectors, take 1 minus this value
    distance = 1 - (len(intersection)/len(union))
    
    return distance



def cosine_sim(x, y):

    # run checks
    if check_for_null(x, y) or check_for_diff_length(x, y):
        return ValueError

    # calculate the dot product of the two vectors
    dot = 0
    for i, j in zip(x,y):
        dot += i*j

    # calculate the magnitude of the two vectors
    mag_x = magnitude(x)
    mag_y = magnitude(y)

    # ignore this, i don't think we have to actually calculate inverse cos, but i could be wrong
    # inverse_cos = acos(dot/(mag_x*mag_y))
    #
    # theta = 1 - inverse_cos
    #
    # print("dot:", dot)
    # print("mag x:", mag_x)
    # print("mag y:", mag_y)
    # print(theta)

    # calculate similarity score
    similarity = dot/(mag_x*mag_y)

    return similarity


# check to make sure there is some input for x and y
def check_for_null(x, y):
    if not x or not y:
        return True
    else:
        return False

# check length of x and y
def check_for_diff_length(x, y):
    if len(x) != len(y):
        return True
    else:
        return False

# calculate the magnitude of each vector using pythagorean theorem
def magnitude(vector):
    mag = 0
    for i in vector:
        mag += i ** 2
    mag = sqrt(mag)
    return mag
