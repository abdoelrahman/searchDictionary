import difflib
text = open("dictionary.txt")
text=text.read()
yourString= input("write here : ")
array=yourString.split()
text=text.split()
def orderedSequentialSearch(alist, item):
    fist=0
    lest= len(alist)-1
    simllar=[]
    while fist<=lest:
        mid=(fist+lest)//2
        if alist[mid] == item:
            return alist[mid]


        else:
            if item< alist[mid]:
                lest=mid-1
            else:
                fist=mid+1
    for i in range(len(alist)):
        if difflib.SequenceMatcher(None, alist[i], item).ratio() > .7:
            simllar.append(alist[i])
            if (len(simllar)>=5):
                break

    return simllar
for i in array:
    print(orderedSequentialSearch(text,i),end=" ")
