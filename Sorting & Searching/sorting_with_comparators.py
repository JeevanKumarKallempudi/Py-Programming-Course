
def distance(cab):
    x = cab[1]
    y = cab[2]
    return(x**2 + y**2)**.5

def extractYear(car):
    return car['year']

def sortCabs(cabs):
    #Code
    cabs.sort(key = distance)

if __name__ == "__main__":
    cabs = [("cab1",1,2),
            ("cab2",2,3),
            ("cab3",1,0),
            ("cab4",0,0),
            ("cab5",5,3)
    ]

    sortCabs(cabs)
    print(cabs)

    # Example2
    cars = [
        {'name': 'Ford', 'year':2022},
        {'name': 'KIA', 'year':2021},
        {'name': 'BMW', 'year':2019},
        {'name': 'Audi', 'year':2020}
    ]
    cars.sort(key = extractYear, reverse = True)
    print(cars)