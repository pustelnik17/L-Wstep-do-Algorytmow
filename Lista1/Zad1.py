import numpy as np
n, m = 5, 5
matrix = np.random.choice([2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5], size=(m, n))
print(matrix)

def failingStudentsCount(matrix, threshold):
    print("\n", "-"*10, "Liczba studentów, którzy nie zaliczyli co najmniej n przedmiotów", "-"*10)
    failingStudentsCount = 0
    for student in matrix:
        failedSubjectCount = 0
        for mark in student:
            failedSubjectCount += 1 if  mark == 2.0 else 0
        failingStudentsCount += 1 if failedSubjectCount >= threshold else 0
    print(failingStudentsCount)
failingStudentsCount(matrix, threshold=2)

def marksOfStudentsMinAndMaxAverage(matrix):
    print("\n", "-" * 10, "Oceny studentów z najniższą i najwyższą średnią", "-" * 10)
    averages = [np.average(matrix[i]) for i in range(len(matrix))]
    print("Minimum AVG: ", matrix[np.argmin(averages)], averages[np.argmin(averages)])
    print("Maximum AVG: ", matrix[np.argmax(averages)], averages[np.argmax(averages)])
marksOfStudentsMinAndMaxAverage(matrix)

def studentWithMaximumNuberOfBestMarks(matrix):
    print("\n", "-" * 10, "Student z najwyższą liczbą ocen najwyższych", "-" * 10)
    bestMark = np.max(matrix)
    bestMarkOccurances = [np.count_nonzero(student == bestMark) for student in matrix]
    print(matrix[np.argmax(bestMarkOccurances)])
studentWithMaximumNuberOfBestMarks(matrix)

def histogram(matrix):
    print("\n", "-" * 10, "Histogramy ocen z poszczególnych przedmiotów", "-" * 10)
    for subject in matrix.T:
        print(np.histogram(subject, [2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5]))
histogram(matrix)

def studentsWithAvgGreaterThan(matrix):
    print("\n", "-" * 10, "Lista studentów ze średnimi nie niższymi niż 4.5", "-" * 10)
    result = []
    averages = [np.average(matrix[i]) for i in range(len(matrix))]
    for studentId in range(len(averages)):
        if(averages[studentId] >= 4.5):
           result.append(matrix[studentId])
    print(result if result != [] else "Brak takich studentów")
studentsWithAvgGreaterThan(matrix)