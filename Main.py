import sklearn

import numpy as np
import pickle
import math
from scipy import spatial
from sklearn import tree, preprocessing
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier

listOfTags = list()
listOfGenres = list()
listOfActors = list()
listOfDirectors = list()
listOfFeatures = list()
userList = list()
movieList = list()
guessedRatings = list()


newfile = 'directorsArray.pk'
with open(newfile, 'rb') as fi:
   listOfDirectors = pickle.load(fi)

newfile = 'genresArray.pk'
with open(newfile, 'rb') as fi:
   listOfGenres = pickle.load(fi)

newfile = 'userList.pk'
with open(newfile, 'rb') as fi:
   userList = pickle.load(fi)

newfile = 'movieList.pk'
with open(newfile, 'rb') as fi:
   movieList = pickle.load(fi)

listOfFeatures = listOfGenres + listOfDirectors
itemProfile = np.zeros([65134,len(listOfFeatures)])

with open("movie_genres.dat","r") as fp:
    line = fp.readline()
    line = fp.readline()
    while line:
        line_vec = line.split()
        itemProfile[int(line_vec[0])][listOfFeatures.index(line_vec[1])] +=1
        line = fp.readline()

with open("movie_directors.dat","r") as fp:
    line = fp.readline()
    line = fp.readline()
    while line:
        line_vec = line.split()
        itemProfile[int(line_vec[0])][listOfFeatures.index(line_vec[1])] +=1
        line = fp.readline()


with open("test.dat","r") as fp:
    counter = 0;
    line = fp.readline()
    line = fp.readline()

    while line:
        counter += 1
        print(counter)
        totalWeights = 0.0
        weightedAverage = 0
        line_vec = line.split()
        testMovieVec = itemProfile[int(line_vec[1])]
        for i in movieList[userList.index(line_vec[0])]:
            trainMovieVec = itemProfile[int(i[0])]
            weight = 1 - spatial.distance.cosine(testMovieVec,trainMovieVec)
            totalWeights += weight
            weightedAverage += weight * float(i[1])
           # print("similarity = " + str(weight))

        guessRating = weightedAverage/totalWeights
        print(guessRating)
        if math.isnan(guessRating):
            guessedRatings.append(3.0)
        else:
            guessedRatings.append(guessRating)
        line = fp.readline()

output_file = open("output1.txt", "w")

for v in guessedRatings:
   output_file.write(str(float(v)) + "\n")