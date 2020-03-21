import math

def in_bounds(goat, house1, house2):
    if house1[0] <= goat[0] <= house2[0]:
        return 'y'
    if house1[1] <= goat[1] <= house2[1]:
        return 'x'
    if house1[0] >= goat[0] >= house2[0]:
        return 'y'
    if house1[1] >= goat[1] >= house2[1]:
        return 'x'
    return False

def min_straight_dist(check, goat, house1, house2):
    if check =='x':
        dist = min(abs(goat[0] - house1[0]), abs(goat[0] - house2[0]))
    
    if check =='y':
        dist = min(abs(goat[1] - house1[1]), abs(goat[1] - house2[1]))
    
    return dist

def two_points_dist(point1, point2):
    dist = math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)
    return dist

def min_corner_dist(goat, house1, house2):
    dist1 = two_points_dist(goat, house1)
    dist2 = two_points_dist(goat, house2)
    dist3 = two_points_dist(goat, [house1[0], house2[1]])
    dist4 = two_points_dist(goat, [house1[1], house2[0]])
    return min(dist1, dist2, dist3, dist4)

def get_min_dist(arr):
    arr = map(int, arr)
    [x, y, x1, y1, x2, y2] = arr
    goat = [x, y]
    house1 = [x1, y1]
    house2 = [x2, y2]
    
    check = in_bounds(goat, house1, house2)
    if check:
        min_rope = min_straight_dist(check, goat, house1, house2)
    else:
        min_rope = min_corner_dist(goat, house1, house2)

    return min_rope

arr = input().split()
print("%.3f" % get_min_dist(arr))
