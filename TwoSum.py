def twoSum(arr, target, n):

    d={}
    for i in arr:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
#     print(d)
    ans2=[]
    for i in arr:
        if target-i==i:
            ans=d[i]//2
            for _ in range(ans):
                ans2.append((i,i))
            d[i]=0
        elif target-i in d:
            ans=min(d[i],d[target-i])

            for _ in range(ans):
                ans2.append((i,target-i))
            d[i]=0
            d[target-i]=0
    if ans2==[]: 
        return [(-1,-1)]  
    else:
        return ans2
            
    return ans2


def takeInput() :

    n, tar = map(int, input().strip().split(" "))
    arr = list(map(int, input().strip().split(" ")))
    return n, tar, arr

def printAns(ans):
    for i in ans:
        if i[0] < i[1]:
            print('{} {}'.format(i[0], i[1]))
        else:
            print('{} {}'.format(i[1], i[0]))

t = int(input().strip())
for i in range(t) :

    n, target, arr = takeInput()

    ans = twoSum(arr, target, n)
    printAns(ans)