def comp(array1, array2):
    if array1 == [] and array2 == []:
        return True
    if not array1 or  not array2:
        return False
    else:
        array1 = sorted(array1)
        array2 = sorted(array2)
        res = []
        for i in array1:
            res.append(i*i)
        print(res)
        if sorted(res) == array2:
            return True
        else:
            return False