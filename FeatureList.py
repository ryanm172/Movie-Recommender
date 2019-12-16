
import numpy as np
import pickle

listOfTags = list()
listOfGenres = list()
listOfActors = list()
listOfDirectors = list()
listOfFeatures = list()
itemProfile = np.zeros([65134,16529])
#ratingArray = np.zeros([71534,65134])
ratingArrayCount = np.zeros(65134)

with open("tags.dat","r") as fp:
    line = fp.readline()
    line = fp.readline()
    while line:
        line_vec = line.split()
        listOfTags.append([line_vec[1]])
        #tagsArray[int(line_vec[0])][int(line_vec[1])] += int(line_vec[2])
        line = fp.readline()
newfile = 'tagsArray.pk'
print(len(listOfTags))
with open(newfile, 'wb') as fi:
  # dump your data into the file
  pickle.dump(listOfTags, fi)
print("1")

with open("movie_genres.dat","r") as fp:
    line = fp.readline()
    line = fp.readline()
    while line:
        line_vec = line.split()
        try:
            listOfGenres.index(line_vec[1])
        except ValueError:
            listOfGenres.append(line_vec[1])

        line = fp.readline()
print("2")
newfile = 'genresArray.pk'
print(len(listOfGenres))
with open(newfile, 'wb') as fi:
  # dump your data into the file
  pickle.dump(listOfGenres, fi)


with open("movie_actors.dat","r") as fp:
    line = fp.readline()
    line = fp.readline()
    while line:
        line_vec = line.split()
        try:
            listOfActors.index(line_vec[1])
        except ValueError:
            listOfActors.append(line_vec[1])
        line = fp.readline()

newfile = 'actorsArray.pk'
print(len(listOfActors))
with open(newfile, 'wb') as fi:
  # dump your data into the file
  pickle.dump(listOfActors, fi)
print("3")

with open("movie_directors.dat", "r") as fp:
    line = fp.readline()
    line = fp.readline()
    while line:
        line_vec = line.split()
        try:
            listOfDirectors.index(line_vec[1])
        except ValueError:
            listOfDirectors.append(line_vec[1])
        line = fp.readline()

newfile = 'directorsArray.pk'
print(len(listOfDirectors))
with open(newfile, 'wb') as fi:
  # dump your data into the file
  pickle.dump(listOfDirectors, fi)

print("4")
#listOfFeatures = listOfTags + listOfActors + listOfGenres + listOfDirectors
#newfile = 'FeatureArray.pk'
#print(len(listOfFeatures))
#with open(newfile, 'w') as fi:
  # dump your data into the file
 # pickle.dump(listOfFeatures, fi)

