"""
插入排序：
对于每一个元素，比较它左边的所有元素，以保证每一次都让其左边所有元素保持升序
优点：对于快排好了元素，复杂度较小
缺点：当数据量大的时候，排后面的元素将花费很大的复杂度
复杂度：best:n
       worst:n^2
       average:n^2
"""
def insertionSort(array):
    for i in range(1,len(array)):
        for j in range(i,0,-1):
            if array[j]<array[j-1]:
                swap(j,j-1,array)
            else:
                break

def swap(a,b,array):
    t=array[a]
    array[a]=array[b]
    array[b]=t


if __name__ == "__main__":
    dateSet=[1,7,8,3,4,5,2,98]
    insertionSort(dateSet)
    print(dateSet)