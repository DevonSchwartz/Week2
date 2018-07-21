'''
Created on Sept 24, 2017

@author: YOUR NAME HERE
'''

answer = []
def process(name):
    # name is a file, returns a list of strings
    #    from the file
    f = open(name)
    for line in f:
        line = line.strip()
        line = line.split(':')
        answer.append(line)
    return answer

def averageHeight(data):
    count = 0
    sub_total = 0
    total = 0
    for i in answer:
        for x in i:
            if x.isdigit() == True:
                count += 1
                sub_total = sub_total + int(x)
    total = sub_total / count

    return total









if __name__ == '__main__':
    filename = "athletes.txt"
    data = process(filename)
    print ("THE DATA IS:")
    for item in data:
        print (item)
    print
print (averageHeight(answer))
