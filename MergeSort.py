"""
归并排序
时间复杂度：nlgn
"""


"""
NTU的merge算法，较为复杂，适合Java中实现
a:未排序的第一部分的第一个元素
b:未排序的第二部分的第一个元素
mid:未排序的第一部分的最后一个元素
每次排序后都要保证后面未排序的部分保持这个标志
"""
def merge_NTU(n,m,array):
    mid=int((n+m)/2)
    a,b=n,mid+1
    if (m-n) <= 0:
        return;
    while a <=mid and b<=m:
        if array[a]>array[b]:
            tmp=array[b]
            b+=1
            mid+=1
            for i in range(mid,a,-1):
                array[i]=array[i-1]
            array[a]=tmp
            a+=1
        elif array[a]<array[b]:
            a+=1
        else:
            if a==mid and b==m:
                break
            tmp=array[b]
            b+=1
            a+=1
            mid+=1
            for i in range(mid,a,-1):
                array[i]=array[i-1]
            array[a]=tmp
            a=a+1


"""
较为简单的merge算法，使用了一个新的list，相对来说空间复杂度较高
"""
def merge(a,b):
    tmp=[]
    h=j=0
    while j<len(a) and h<len(b):
        if a[j]<b[h]:
            tmp.append(a[j])
            j+=1
        else:
            tmp.append(b[h])
            h+=1
    if j==len(a):
        for i in b[h:]:
            tmp.append(i)
    else:
        for i in a[j:]:
            tmp.append(i)
    return tmp
        
    

def mergeSort(array):
    if len(array) <=1:
        return array
    mid = int(len(array)/2)
    left = mergeSort(array[:mid])
    right=mergeSort(array[mid:])
    return merge(left,right)

if __name__=="__main__":
    # a=[10,25,71,84,22,25,90,94]
    # merge_NTU(0,7,a)
    a=[1,3,7,33,22,54,2,9]
    print(mergeSort(a))
