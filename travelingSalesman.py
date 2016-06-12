# run this file in the same directory as CitiesCoordinates.txt

def travelingSalesman(airports, coordinates):
    # YOUR CODE HERE - try to return a list of airports with the shortest path.
    # pathDistance([list of cities in specific order], coordinates) will
    # return the overall distance it took to travel to those cities in that
    # order.
    # airports is a list of the cities to be used
    # Try to use all the cities in the list airports

def distance(airPort1, airPort2):
    '''used in pathDistance'''
    x1, x2, y1, y2 = airPort1[0], airPort2[0], airPort1[1], airPort2[1]
    return ((x1-x2)**2+(y1-y2)**2)**0.5

def pathDistance(path, coordinates):
    '''Takes in coodinates dictionary and list of airports. Returns total distance of that path.'''
    # Example usage: pathDistance(['SFO', 'AUS', 'MEM', 'SFO'], coordinates) or pathDistance(testPath, coordinates)
    totalDistance = 0
    for i, item in enumerate(path):
        try:
            totalDistance += distance(coordinates[item],coordinates[path[i+1]])
        except Exception as e:
            print(e)
    return totalDistance

if __name__ == '__main__':
    
    airports = open('CitiesCoordinates.txt','r')
    airportList = [] #List of string of airport 3 letter symbols
    coordinates = {} #Dictionary of airport coordinats i.e. {'SEA': (-123.44, 45), 'SFO':(-122,30),...}
    for airport in airports:
        airport = airport[:-1].split(': ')
        airportList += [airport[0]]
        airport[1] = eval(airport[1])
        coordinates[airport[0]] = airport[1] #Makes coordinates dictionary

    print(travelingSalesman(airportList, coordinates))


