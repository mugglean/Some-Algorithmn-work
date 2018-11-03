"""
堆排序：复杂度nlgn
好处：取前k个最大的元素的时候可以减少运算
"""

def swap(n,m,arr):
    tmp=arr[n]
    arr[n]=arr[m]
    arr[m]=tmp


def heapify(arr,i,length):
    temp=arr[i]
    # k为左边第一个子节点
    k=2*i+1
    while k<length:
        # k为最大的子节点
        if k+1<length and arr[k+1]>arr[k]:
            k+=1
        # i的目的是存储最终要放置的位置
        if arr[k]>temp:
            arr[i]=arr[k]
            i=k
        else:
            break
        k=2*k+1
    arr[i]=temp
    


def heapSort(arr):
    # 从最后一个非叶子节点开始往上构建堆
    for i in range(int(len(arr)/2)-1,-1,-1):
        heapify(arr,i,len(arr))
    # 开始堆排序
    for i in range(len(arr)-1,0,-1):
        swap(0,i,arr)
        heapify(arr,0,i)


if __name__=="__main__":
    arr=[9,8,7,6,5,4,3,2,1]
    heapSort(arr)
    print(arr)