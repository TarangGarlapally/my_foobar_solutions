import math
def solution(s):
    n = int(s)
    res = (n*(n+1)//2)*math.sqrt(2)

    res -= (n//2)

    res = math.floor(res)
    return str(int(res))
def solution2(s):
    n = int(s)
    res = 0


    for i in range(1,n+1):
        res += math.floor(i*math.sqrt(2))

    return str(int(res))

extras = 0
wf = 0
min_extras = 1
idx = -1
for i in range(1,10000):
    a = i*math.sqrt(2)
    wf += a
    redundant = a - math.floor(a)
    extras += redundant
    
    #print(a,"r:",redundant, "1's",extras, i, "ans:",solution2(i),"wf:",wf,"myans:",solution(i),"sum:",i*(i+1)//2, sep = "\t")
    #print(i,"a:",a, "1's",extras,"wf:", wf, "ans:", solution2(i),"myans:", solution(i),sep="\t")
    if(i%70 == 0):
        print("-"*70)
        print("ones:", extras)
        print("-"*70)
    x = extras - math.floor(extras)
    if(x<min_extras):
        min_extras = x
        idx = i
print(min_extras,idx)
n=1000
s = 1000//70
s=s*70
redundant = 0
extras = 0
#after 70 multiples
for i in range(s+1,n+1):
    a = i*math.sqrt(2)
    redundant = a - math.floor(a)
    extras += redundant
    print(i,extras)
