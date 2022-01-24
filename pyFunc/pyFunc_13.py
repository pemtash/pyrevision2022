def printStudentDetails(name, age, marks, stream):
    print('Student details')
    print('Name: {}, Age: {}, Marks: {}, Stream: {}'.format(
        name, age, marks, stream
    ))


printStudentDetails('pema', 28, 300, 'Datasci')


#unpacking
d = {'name': "john", "stream": "ece", 'age': 17, 'marks': 700}
printStudentDetails(**d)
# printStudentDetails(*d) is not the right way

