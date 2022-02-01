if __name__ == '__main__':
    a = [1,2,3,4,5,6,7]

    # Method 1:
    # print(a[::-1])

    # Method 2:
    # i = 0
    # j = len(a)-1
    # while i < j:
    #     a[i],a[j]=a[j],a[i]
    #     i+=1
    #     j-=1
    # print(a)

    # Method 3:
    print(list(reversed(a)))
