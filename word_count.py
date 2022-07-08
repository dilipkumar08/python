def cleaning_data(sentence,symbols,word):
for item in symbols:
        cd=sentence.replace(item,'')
    sorted_data=cd.lower()
    sorted_data=sorted_data.split()
    count_data=[]
    for w in sorted_data:
        count_data.append(sorted_data.count(w))
    dcd=dict(list(zip(sorted_data,count_data)))
    word=word.lower()
    if word in dcd.keys():
        return(dcd[word])
    else:
        return 0

if __name__=="__main__":
    input_string = "She sells seashells on the sea shore. The shells she sells are seashells, I'm sure. And if she sells seashells on the sea shore, Then I'm sure she sells seashore shells."
    symbols=[',',';','.']    
    word='then'
    print(cleaning_data(input_string,symbols,word))
    
        
