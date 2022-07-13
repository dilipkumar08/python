def count_substring(string, sub_string):
    l=len(sub_string)
    b=0
    c=[]
    la=len(string)
    for i in range(la):
        if string[b:l]==sub_string and l<=la:
            c.append(string[b:l])
        b=b+1
        l=l+1
    return len(c)

if __name__ == '__main__':
    string = raw_input().strip()
    sub_string = raw_input().strip()
    
    count = count_substring(string, sub_string)
    print count
