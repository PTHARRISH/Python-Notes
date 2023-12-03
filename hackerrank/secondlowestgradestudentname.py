if __name__ == '__main__':
    records=[]
    scorelist=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
        scorelist.append(score)
    b=sorted(list(set(scorelist)))[1]
    
    for a,c in sorted(records):
        if c==b:
            print(a)
            
