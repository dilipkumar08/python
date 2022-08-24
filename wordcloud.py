from wordcloud import WordCloud
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import *
from tkinter.filedialog import askopenfilename    

def wordcount(freq):
    w=int(input("\nEnter the width for the image: "))
    h=int(input("\nEnter the height for the image: "))
    bc=str(input("\nEnter the background color: "))    
    wc = WordCloud(width=w, height=h, max_words=1000, background_color=bc).generate_from_frequencies(freq)
    plt.figure(figsize=(12, 8))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.show()
    
if '__main__'==__name__:
    manual_data=[]
    print("\t\tEnter a method to add your words")
    try:
        option=(int(input("\n1,choose file 2,manual inputs  :")))
    except:
        option=(int(input("\n[Enter only the digits ('1'or'2') to choose a option]\n\n1,choose file 2,manual inputs  :")))
    if option==1:
        print("\nThe file should only be in a sperated format with a unique symbol")
        s=str(input("\nEnter the seperator type for example [' ' or ',' or ';' ] :"))
        location=askopenfilename()
        data=pd.read_csv(location,encoding = 'ISO-8859-1',header=None,sep=s,on_bad_lines='skip',engine='python')
        print(data)
        freq=pd.Series(manual_data).value_counts()
        print(freq)
        wordcount(freq)           
    elif option==2:
        n=int(input("\nEnter the number of word you would like to Add: "))
        for i in range(n):
            m=str(input("Enter word "+str(i+1)+" :"))
            manual_data.append(m)
        freq=pd.Series(manual_data).value_counts()
        wordcount(freq)
    while True:
        try:
            change=int(input("\nType '1' to change the size or background color:"))
            if change==1:
                wordcount(freq)
                else:
                    break
        except:
            break
    print("\nDo you wanna Download the image")
    yn=int(input("\nif 'yes' type '1' :"))
    if yn==1:
        print("\nEnter the file with it's format ex:image.png\n")
        name=str(input())
        plt.savefig(name)
                    
    
    
