arr=[352, 210, 55, 137, 86, 493, 494, 407, 74, 332, 343, 91, 305, 238, 286, 199, 202, 477, 257, 360, 118, 326, 491, 92, 483,
     163, 204, 240, 354, 54, 148, 371, 393, 493, 353, 84, 153, 184, 41, 103, 24, 147, 92, 83, 417, 440, 274, 186, 242, 119,
     483, 425, 202, 421, 387, 486, 201, 226, 357, 236, 469, 17, 247, 45, 490, 409, 88, 262, 52, 216, 348, 410, 379, 471, 343,
     7, 304, 478, 277, 334, 318, 166, 389, 237, 399, 496, 25, 496, 140, 258, 461, 103, 98, 308, 249, 89, 23, 8, 64, 414, 209,
     169, 246, 376, 152, 122, 1, 380, 38, 59, 364, 60, 34, 227, 332, 43, 317, 349, 244, 365, 421, 288, 87, 15, 383, 0, 387,
     302, 88, 426, 260, 60, 450, 55, 13, 478, 72, 338, 110, 297, 291, 358, 395, 278, 478, 37, 111, 208, 432, 10, 373, 69,
     417, 232, 483, 492, 258, 372, 416, 145, 497, 225, 260, 337, 401, 426, 25, 387, 349, 212, 85, 167, 299, 360, 485, 494,
     419, 179, 167, 67, 284, 248, 263, 209, 179, 90, 271, 60, 261, 275, 81, 4, 11, 11, 94, 119, 284, 301, 379, 167, 413, 419,
     18, 173, 166, 445, 310, 212, 375, 88, 80, 340, 282, 335, 23, 348, 206, 17, 209, 329, 295, 492, 186, 197, 336, 318, 159,
     133, 157, 206]


def heapInsert(arr,index):
    while arr[index]>arr[(index-1)//2] and index>0:
        arr[index],arr[(index-1)//2]=arr[(index-1)//2],arr[index]
        index=(index-1)//2

def heapify(arr,index,heapsize):
    left=index*2+1
    while left<heapsize:
        if left+1<heapsize and arr[left]<arr[left+1] :
            largest=left+1
        else:
            largest=left
        if arr[largest]<arr[index]:
            return
        arr[largest],arr[index]=arr[index],arr[largest]
        index=largest
        left=index*2+1

def heapSort(arr):
    if len(arr)<2:
        return

    # for i in range(len(arr)-1,-1,-1):
    #     heapify(arr,i,len(arr))

    for i in range(len(arr)):
        heapInsert(arr,i)

    heapsize=len(arr)-1
    arr[0],arr[heapsize]=arr[heapsize],arr[0]
    while heapsize>0:
        heapify(arr,0,heapsize)
        heapsize-=1
        arr[0],arr[heapsize]=arr[heapsize],arr[0]

heapSort(arr)
print(*arr)
