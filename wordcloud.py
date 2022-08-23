from wordcloud import WordCloud
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import *
from tkinter.filedialog import askopenfilename    


def wordcount(freq):
    w=int(input("Enter the width for the image:"))
    h=int(input("Enter the height for the image:"))
    bc=str(input("Enter the background color"))    
    wc = WordCloud(width=w, height=h, max_words=10000, background_color=bc).generate_from_frequencies(freq)
    plt.figure(figsize=(12, 8))
    plt.imshow(wc, interpolation='bilinear')

    if '__main__'==__name__:
    manual_data=[]
    print("\t\tEnter a method to add your words")
    try:
        option=(int(input("1,choose file 2,manual inputs  :")))
    except:
        option=(int(input("[Enter only the digits ('1'or'2') to choose a option]\n\n1,choose file 2,manual inputs  :")))
    if option==1:
        print("The file should only be in a sperated format with a unique symbol")
        s=str(input("Enter the seperator type for example [' ' or ',' or ';' ] :"))
        location=askopenfilename()
        data=pd.read_csv(location,encoding = 'ISO-8859-1',header=None,sep=s,error_bad_lines=False,engine='python')
        print(data)
        freq=pd.Series(manual_data).value_counts()
        print(freq)
        wordcount(freq)
    elif option==2:
        n=int(input("Enter the number of word you would like to Add: "))
        for i in range(n):
            manual_data.append(str(input("Enter word",n,":")))
        freq=pd.Series(manual_data).value_counts()
        wordcount(freq)
        
    while True:
        change=int(input("Type '1' to change the size or background color:"))
        if change==1:
            wordcount(freq)
        else:
            break
    print("Do you wanna Download the image")
    yn=int(input("if 'yes' type '1' :"))
    if yn==1:
        print("Enter the file with it's format ex:image.png")
        name=str(input())
        plt.savefig(name)
                    
    
    
