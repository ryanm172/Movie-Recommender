import numpy as np
import pickle

listOfTags = list()
listOfGenres = list()
listOfActors = list()
listOfDirectors = list()
listOfFeatures = list()
itemProfile = np.zeros([65134,16529])

newfile = 'directorsArray.pk'
with open(newfile, 'rb') as fi:
   listOfDirectors = pickle.load(fi)
newfile = 'genresArray.pk'

newfile = 'genresArray.pk'
with open(newfile, 'rb') as fi:
   listOfGenres = pickle.load(fi)

listOfFeatures = listOfGenres + listOfDirectors

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

newfile = 'IPGenDirec.pk'

with open(newfile, 'wb') as fi:
    pickle.dump(itemProfile, fi)