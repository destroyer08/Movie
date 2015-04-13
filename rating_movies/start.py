import re
import imdb
from decimal import Decimal
import operator
from math import sqrt
from unicodedata import decimal
def show(dic,s):
    print("\n\n********{}********\n".format(s))
    for key, rating in dic.iteritems():
        print("{} {}".format(key,rating))
def show_watched(dic):
    print("\n\n********YOUR WATCHED MOVIES AND RATING********\n")
    for key, rating in dic.iteritems():
        print("{} {}".format(key,rating))
    
def show_all(dic,dic2):
    print("\n\n********YOUR WATCHED MOVIE RATING WITH IMDB RATING********\n")
    for title in dic.iterkeys():
        print("{} {} {}".format(str(title).strip(),dic[title],dic2[title]))

def show_all_norm(dic,dic2):
    print("\n\n********YOUR WATCHED MOVIE RATING WITH IMDB RATING(NORMALIZE)********\n")
    for title in dic.iterkeys():
        print("{} {} {}".format(str(title).strip(),dic[title],dic2[title]))

def show_watch(dic3):
    print("\n\n********YOUR WANT TO WATCH MOVIES WITH IMDB RATING********\n")
    for title in dic3.iterkeys():
        print("{} {}".format(str(title).strip(),dic3[title]))
        
def show_dev(dev):
    print("\n\n********DEVIATIONS********\n")
    for t1, ele in dev.iteritems():
        print("---------------------------")
        print(t1)
        print("---------------------------")
        for t2, d in ele.iteritems():
            print("{} {}".format(t2, d))

def show_pred(predict):
    print("\n\n********PREDICTED RATING********\n")
    #predict = sorted(predict.items(),key = operator.itemgetter(1))
    for t, rate in predict.iteritems():
        print("{} {}".format(t,rate))
       
def get_imdb_rating(dic):
    ia = imdb.IMDb()
    dic2 = {}
    for title in dic.iterkeys():
        t = str(title).strip()
        s_result = ia.search_movie(t)
        the_unt = s_result[0]
        ia.update(the_unt)
        irate = the_unt["rating"]
        dic2[title] = irate
        #print("{} {}".format(t,irate))
    return(dic2)
def get_imdb_rating_watch(watch):
    ia = imdb.IMDb()
    dic3 = {}
    for title in watch:
        t = str(title).strip("\n")
        s_result = ia.search_movie(t)
        the_unt = s_result[0]
        ia.update(the_unt)
        irate = the_unt["rating"]
        dic3[t] = irate
        #print("{} {}".format(t,irate))
    return(dic3)
def norm(dic2,omin,omax,nmin,nmax):
    con_dic = {}
    oRange = omax - omin
    nRange = nmax - nmin
    for title,rating in dic2.iteritems():
        NewValue = (((rating - omin) * nRange) / oRange) + nmin
        con_dic[title] = Decimal(str(NewValue)).quantize(Decimal('0.01'))
    return(con_dic)

def devi(dic2,dic3):
    
    dev = {}
    for t1,r1 in dic3.iteritems():
        temp ={}
        for t2,r2 in dic2.iteritems():
            temp[t2] = r1-r2
        dev[t1] = temp
    return(dev)

def pred(dev,dic):
    predict = {}
    for t1, elem in dev.iteritems():
        num = 0
        den = 0
        for t2, d in elem.iteritems():
            num += dic[t2] + d
            den += 1
        predict[t1] = num/den
    return(predict)
def get_imdb_cate(dic):
    ia = imdb.IMDb()
    dic2 = {}
    for title in dic.iterkeys():
        
        t = str(title).strip()
        s_result = ia.search_movie(t)
        the_unt = s_result[0]
        ia.update(the_unt)
        irate = the_unt["genre"]
        for item in irate:
            if item in dic2:
                dic2[item].append(title)
            else:
                dic2[item]=[title]
        
   
    return(dic2)

def get_imdb_cate_watch(dic):
    ia = imdb.IMDb()
    dic2 = {}
    for title in dic.iterkeys():
        
        t = str(title).strip()
        s_result = ia.search_movie(t)
        the_unt = s_result[0]
        ia.update(the_unt)
        irate = the_unt["genre"]
        dic2[title] = irate
    return(dic2)

def cal_score(dic3,cos,predict):
    temp ={}
    res = {}
    for key,val in dic3.items():
        t = 0
        c = 0
        for cat in val:
            if cat in cos:
                t += cos[cat]
                c += 1
        if(c >0):
            temp[key] = t/c
        else:
            temp[key] = c
    for key,val in predict.iteritems():
        res[key] = float(val) + float(temp[key])
    return(res)
    
    
def get_cosine(cate,dic):
    cos = {}
    for k,v in cate.items():
        usum = 0
        csum = 0
        prod = 0
        for item in dic:
            a = dic[item]
            usum += a*a
        for item in v:
            a = dic[item]
            csum += 5*5
            prod += 5*a
        total = prod/(sqrt(usum)*sqrt(csum))
        cos[k] = total
    return(cos)
    
file = open("watched.txt","r")
file2 = open("want_to.txt","r")

s = file.readline()
#n= map(int,re.findall("\s+", s))
dic = {}
while(s):
    rating = map(int,re.findall("\d+",s,))
    temp = re.findall("\S+", s,)
    m = len(temp)
    s = ""
    for i in range(m-1):
        s+= temp[i]+" "
    s = str(s.strip())
    dic[s] = rating[0]
    s = file.readline()
s = file2.readline()
watch = []
while(s):
    watch.append(s)
    s = file2.readline()

dic3 = get_imdb_rating_watch(watch)
dic2 = get_imdb_rating(dic)
con_dic2 = norm(dic2,1,10,1,5)
con_dic3 = norm(dic3,1,10,1,5)
dev = devi(con_dic2, con_dic3)
show(dic,"YOUR WATCHED MOVIES AND RATING")
show_all(dic,dic2)
show_all_norm(dic, con_dic2)
show_watch(con_dic3)
show_dev(dev)
predict = pred(dev, dic)
show_pred(predict)
#show_all()'
cate = get_imdb_cate(dic)
show(cate,"WATCHED MOVIES WITH CATEGORIES")
cos = get_cosine(cate,dic)
show(cos,"SCORE OF EACH CATEGORY")
watch_cate = get_imdb_cate_watch(dic3)
show(watch_cate,"MOVIES WANT TO WATCH WITH CATEGORIES")
rec_score = cal_score(watch_cate,cos,predict)
show(rec_score,"FINAL RATING")
final = norm(rec_score,0,6,0,1)
show(final,"RECOMMENDATION SCORE")
