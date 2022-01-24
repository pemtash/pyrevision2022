# Args

def printPlayerDetails(name, age, team):
    print('Player Details: ')
    print('name: {}, Age: {}, Team: {}'.format(name, age, team))

printPlayerDetails('Virat', 33, "rcb")


msd = ("ms dhoni", 37, 'csk')
printPlayerDetails(msd[0], msd[1], msd[2])

printPlayerDetails(*msd)

# packaging and unpackaging
# args

