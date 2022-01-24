# kwargs ==> Dictionary


def printStudentDetails(**kwargs):
    print('kwargs: ', kwargs)
    print('type(kwargs) : ', type(kwargs))
   # print("Student Details: Name: {}, Age: {}, Marks: {}, Stream: ".format(
    #   kwargs['name'], kwargs['age'], kwargs['marks'], kwargs['stream']
    #))

#printStudentDetails("mary", 15, 500, 'cse')
#printStudentDetails(name="mary", age=15, marks=500, stream='cse')


d = {'name': "john", "stream": "ece", 'age': 17, 'marks': 700}
print('id(d): ', id(d))
printStudentDetails(**d)
