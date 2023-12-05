# Rome Letters To Integer
def rometoint(s):
        d={
            "I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000
        }
        sums=0
        for i in range(len(s)):
            if i<len(s)-1 and d[s[i]]<d[s[i+1]]:
                sums-=d[s[i]]
            else:
                sums+=d[s[i]]
        # i=0
        # sums=0
        # while i<len(s)-1:
        #     if d[s[i]]>=d[s[i+1]]:
        #         sums+=d[s[i]]
        #         i+=1
        #     else:
        #         sums+=d[s[i+1]]-d[s[i]]
        #         i+=2
        # if i==len(s)-1:
        #     sums+=d[s[i]]
        return sums

print(rometoint("XII"))