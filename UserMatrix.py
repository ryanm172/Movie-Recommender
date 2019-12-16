
import numpy as np
import pickle
ratingList = list()
userList = list()
movieList = list()

with open("train.dat","r") as fp:
    line = fp.readline()
    line = fp.readline()
    while line:
        line_vec = line.split()
        try:
            userList.index(line_vec[0])
        except ValueError:
            userList.append(line_vec[0])
         #   print(userList)
            movieList.append(list())

        movieList[userList.index(line_vec[0])].append([line_vec[1],line_vec[2]])
       # ratingList[userList.index(line_vec[0])][movieList[userList.index(line_vec[0])].index(line_vec[1])]

        #tagsArray[int(line_vec[0])][int(line_vec[1])] += int(line_vec[2])
        line = fp.readline()

newfile = 'userList.pk'
with open(newfile, 'wb') as fi:
  # dump your data into the file
  pickle.dump(userList, fi)

newfile = 'movieList.pk'
with open(newfile, 'wb') as fi:
  # dump your data into the file
  pickle.dump(movieList, fi)

