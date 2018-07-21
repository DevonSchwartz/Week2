'''
Created on Sep 17, 2017

@author: YOUR NAME HERE
'''

answer_1 = []

def process(name):
    f = open(name)
    for line in f:
        line = line.strip()
        line = line.split(';')
        answer_1.append(line)
    return answer_1

def classAverage(data):
    count = 0
    sub_total = 0
    total = 0
    for i in answer_1:
        for x in i:
            if x.isdigit() == True and int(x) <= 100:
                count += 1
                sub_total = sub_total + int(x)
    total = sub_total / count

    return total

def maxGrade(data):
    grades = []
    for i in answer_1:
        for x in i:
            if x.isdigit() == True and int(x) <= 100:
                grades.append(int(x))

    grades = sorted(grades)
    return (grades[-1])

def howManyInRange(data, year1, year2):
    years = []
    for i in answer_1:
        for x in i:
            if x.isdigit() == True:
                if int(x) >= year1 and int(x) <= year2:
                    years.append(x)

    return len(years)

def namesForGrades(data, grade1, grade2):
    names = []
    for i in answer_1:
        for x in i:
            if x.isdigit() == True and int(x) <= 100:
                if int(x) >= grade1 and int(x) <= grade2:
                    if x in i:
                        names.append(i[0])
    return names

if __name__ == '__main__':
    filename = "grades.txt"
    data = process(filename)
    for each in data:
        print (each)
    print

    print ("Average grade is ", classAverage(data))
    print ("Maximum grade is ", maxGrade(data))
    grade1 = eval(input("What Grade?: "))
    grade2 = eval(input("What Grade?: "))
    print ("Names of people with grades between ", grade1, " and ", grade2, " inclusive")
    names = (namesForGrades(data, grade1, grade2))
    print (names)
    # ADD CODE TO PRINT the names one per line
    #print
    #year1 = eval(input("What Year?: "))
    #year2 = eval(input("What Year?: "))
    #print ("Number born from ",year1,"to",year2,"is",)
    #print (howManyInRange(data, year1, year2))
