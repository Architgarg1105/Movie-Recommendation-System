import pandas as pan
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import difflib

def title(index):
    return movie[movie.index == index]["title"].values[0]

def genres(index):
    return movie[movie.index == index]["genres"].values[0]

def directors(index):
    return movie[movie.index == index]["director"].values[0]

def homepages(index):
    return movie[movie.index == index]["homepage"].values[0]

def vote_averages(index):
    return movie[movie.index == index]["vote_average"].values[0]

def index(title):
    titleList = movie['title'].tolist()
    commonPart = difflib.get_close_matches(title,titleList,1)
    similarTitle = commonPart[0]
    return movie[movie.title == similarTitle]["index"].values[0]

movie = pan.read_csv("moviedata.csv")
movie['vote_average']=movie['vote_average'].astype('str')
features = ['keywords','cast','genres','director','tagline','vote_average']
for feature in features:
    movie[feature] = movie[feature].fillna('')

def combine_features(row):
    try:
        return row['keywords'] +" "+row['cast']+" "+row['genres']+" "+row['director']+" "+row['tagline']+" "+row['vote_average']
    except:
        print ("Error:", row)


def recommend(userInputMovie):
    movie["combined_features"] = movie.apply(combine_features,axis=1)
    cv = CountVectorizer()
    countMatrix = cv.fit_transform(movie["combined_features"])
    cosineSimilarity = cosine_similarity(countMatrix) 
    movieIndex = index(userInputMovie)

    similarMovies = list(enumerate(cosineSimilarity[movieIndex]))
    similarMoviesSorted = sorted(similarMovies,key=lambda x:x[1],reverse=True)
    i=0
    list1=[]
    list2=[]
    list3=[]
    list4=[]
    list5=[]
    for recommendedMovie in similarMoviesSorted:
            if(i!=0):
                list1.append(title(recommendedMovie[0]))
                list2.append(genres(recommendedMovie[0]))
                list3.append(directors(recommendedMovie[0]))
                list4.append(homepages(recommendedMovie[0]))
                list5.append(vote_averages(recommendedMovie[0]))
            i=i+1
            if i>10:
                break
    return list1,list2,list3,list4,list5