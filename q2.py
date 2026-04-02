def remove_adjacent_duplicates(s):
    '''
    Given a string remove all the adjacent duplicate characters and return the string
    '''
    result=""
    i=0
    while i<len(s):
        if len(result)>0 and result[len(result)-1]==s[i]:
            result=result[:len(result)-1]
        else:
            result+=s[i]
        i+=1
    return result