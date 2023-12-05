# Find the Percentage of the student name
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()# student name search average
    i=0
    d=student_marks[query_name]
    i=sum(d)/3

    print("%.2f"%i)

    # using for loop enumerate function 
    # for j,k in enumerate(d):
    #     i+=k
    # i=i/3

    # print("%.2f"%i)
