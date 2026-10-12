def statistik (data):
    total = 0
    minimum = data [0]
    maximum = data [0]
    for x in data:
        if x < minimum:
            minimum = x
        if x > maximum:
            maximum = x
    rata = total / len (data)
    return minimum, maximum, rata

mn, mx , rt = statistik ([170, 80, 65, 90, 75])
print (mn, mx, rt)