def srt(lst):
    res=[]
    maxam=0
    for i in range(len(lst)):
        if maxam<i:
            maxam=i
            res.append(maxam)
        else:
            res.append(maxam)
    return res


lst=[4,7,2,9,1,8,3,6,5]
res=srt(lst)
print(res)