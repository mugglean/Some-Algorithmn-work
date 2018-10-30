"""
快速排序
mainIdea:选中一个pivot,使得小于pivot的都在左边，大于pivot的都在右边，再使用分治思想
最好时间复杂度：每次取的pivot刚好在list的中间，每次都以中间分割，跟归并排序类似，复杂度为nlgn
最坏时间复杂度：每次取的pivot都为最后一个或者第一个，这样的话对另外n-1个继续分治，复杂度为(n-1)+(n-2)+(n-3)+...+1，即n^2
平均：nlgn
优点：不用merge，速度快
缺点：数据量少时速度慢，跟merge一样
"""

def quickSort(n,m,arr):
    if n<m:
        pivot_pos=partition(n,m,arr)
        quickSort(n,pivot_pos-1,arr)
        quickSort(pivot_pos+1,m,arr)
    

"""
选择中间的元素作为快排的pivot元素,last_small为最后一个小于pivot的元素
先把pivot移到最前面，方便用循环对后面的元素进行对比
"""
def partition(n,m,arr):
    mid=int((n+m)/2)
    swap(n,mid,arr)
    pivot=arr[n]
    last_small=n
    for i in range(n+1,m+1):
        if arr[i]<pivot:
            last_small+=1
            swap(last_small,i,arr)
    swap(n,last_small,arr)
    return last_small


    

def swap(n,m,arr):
    tmp=arr[n]
    arr[n]=arr[m]
    arr[m]=tmp


if __name__=="__main__":
    a=[1,8,100,2,99]
    b=[1,2,13,4,5]
    quickSort(0,4,b)
    print(b)