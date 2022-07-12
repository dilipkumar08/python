if __name__ == '__main__':
    students=[]
    for d in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
    students=sorted(students)
    a=[]
    for i in range(len(students)):
        a.append(students[i][1])
        m=min(a)
    while(min(a)==m):
        a.remove(m)
        mi=min(a)
    r=[]
    for i in range(len(students)):
        if mi == students[i][1]:
            print(students[i][0])
