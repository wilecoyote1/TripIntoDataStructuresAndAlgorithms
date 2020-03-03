def searchtext(text, find):
    for i in range(len(text)):
        if text[i] == find[0]:
            isEqual = True
            for j in range(1,len(find)):
                if text[i+j] != find[j]:
                    isEqual = False
                    break
            if isEqual:
                return i
    return -1