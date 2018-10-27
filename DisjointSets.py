"""
使用时间复杂度较小的方法解决两个集合的是否互斥问题
集合a={2,4,8,6,10},b={1,6,3,9}
方法一：比较a的元素和b的元素，n^2复杂度
方法二：对方法一排序,nlgn复杂度，对于b的元素，使用二分搜索来在a的集合中找，复杂度nlgn
"""
# binarySearch,返回index(从0开始计)
def binarySearch(destlist,ele):
    left=0
    right=len(destlist)-1
    while left<=right:    
        mid=int((left+right)/2)
        if destlist[mid] == ele:
            return mid
        elif destlist[mid] > ele:
            right=mid-1
        else:
            left=mid+1
    return -1



if __name__ == "__main__":
    a=[2,10,8,6,13]
    b=[1,6,3,9]
    a.sort()
    disjointFlage=True
    for i in b:
        if binarySearch(a,i)!= -1:
            print("not disjoint")
            disjointFlage=False
            break
    if disjointFlage:
        print("disjoint")