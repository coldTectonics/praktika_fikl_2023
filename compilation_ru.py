#import fasttext
#import langdetect
import nltk
from nltk.tokenize import word_tokenize
import re
import os
from datetime import date
import time


nltk.download('punkt')


def headingsFind (txt_string, re_string, sub_string): #эти три переменные нужно определить в начале main
    s = open(txt_string, "r")
    s = s.read ()

    p = re.compile(re_string, re.MULTILINE)

    q = p.findall(s) #q - заголовки
    #print (q)

    s = re.sub(sub_string, '', s)
    s = re.split(p, s) #s - текст глав
    
    result = []
    result.append (q)
    result.append (s[1:])
    
    #print ("отработало headingsFinds\n")
    #print (result)
    return result #[заголовки, текст глав]


def tokenizationFunc (stringer, x):
    tokens = word_tokenize (stringer, language='czech')

    
    czech_list = []

    i = 0

    
    while i < len(tokens):

        #x = str((model.predict(tokens[i], k=1)))
        if (re.search(r'^[ěščřžýáíéóúůďťňĎŇŤŠČŘŽÝÁÍÉÚŮĚÓa-zA-Z]*$', tokens[i]) != None) & (len(tokens[i]) > 1):  
            if (tokens[i]+'\n') in x:
                czech_list.append (tokens[i])
        i+=1

    mystring = ''
    for x in czech_list:
        mystring += x + '\n'

    print (mystring)

    return mystring #пойдёт на вход в makedir как stringer


def makeDirectory (today, headings, stringer): #финальная экзекуция
    print ("работает mkdir\n")
    dirname = str(today)
    path = './' + dirname
    os.mkdir(path)

    i = 0
    while i < len(headings):
        txtpath = dirname + '/' + headings[i] + '.txt'

        with open(txtpath, 'w') as f:
            f.write(stringer[i])
        i+=1


if __name__ == "__main__":
    t = time.localtime()    
    #model = fasttext.load_model('lid.176.bin')
    #определить: today, ввести txt_string, re_string, sub_string 
    today = str(date.today()) + ' ' + str(time.strftime("%H:%M:%S", t)) 

    txt_string = input("Please enter a filename:\n") #4.txt
    #re_string = input("Please enter regex:\n") #^\d+\. +\S+[ \S+]+$
    re_string = '^\d+\. +\S+[ \S+]+$'
    sub_string = input("Please enter a substituted string:\n") #T&P Books. Русско-чешский тематический словарь. 9000 слов

    head_n_text = headingsFind (txt_string, re_string, sub_string)
    head = head_n_text[0]
    text = head_n_text[1]
    #print ('работает main\n', head, text, len(text))
    head_n_text = []

    text_tokenized = []
    i = 0
    x = open("cs_CZ_1.txt", "r")
    x = x.read ()
    while i < len(text):
        text_tokenized.append (tokenizationFunc (text[i], x))
        i+=1
    #print (text_tokenized)
    makeDirectory (today, head, text_tokenized) 
