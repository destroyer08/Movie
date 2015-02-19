import re
import imdb
def show_watched(dic):
    print("\n\n********YOUR WATCHED MOVIES AND RATING********\n")
    for key, rating in dic.iteritems():
        print("{} {}".format(key,rating))
    
def show_all(dic,dic2):
    print("\n\n********YOUR WATCHED MOVIE RATING WITH IMDB RATING********\n")
    for title in dic.iterkeys():
        print("{} {} {}".format(str(title).strip(),dic[title],dic2[title]))

def show_watch(dic3):
    print("\n\n********YOUR WANT TO WATCH MOVIES WITH IMDB RATING********\n")
    for title in dic3.iterkeys():
        print("{} {}".format(str(title).strip(),dic3[title]))
       
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
        dic3[title] = irate
        #print("{} {}".format(t,irate))
    return(dic3)

        
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
    dic[s] = rating[0]
    s = file.readline()
s = file2.readline()
watch = []
while(s):
    watch.append(s)
    s = file2.readline()
#dic3 = get_imdb_rating_watch(watch)
#dic2 = get_imdb_rating(dic)
show_watched(dic)
#show_all(dic,dic2)

#show_watch(dic3)
#show_all()'

