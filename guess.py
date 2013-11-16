import sys, datetime, numpy, math
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
dataset = sys.argv[1] #the .csv file we are reading form
limitStart= int(sys.argv[2]) #the first data point we are looking at
limitLength = int(sys.argv[3]) # how many subsequent datpoint we should look at

# Import dataset
total = numpy.genfromtxt(dataset, delimiter=',')
data = total[limitStart:limitStart+limitLength, 0:-2]
targets = total[limitStart:limitStart+limitLength, -1]

# Train
rbf = svm.SVC(kernel='rbf')
knn = KNeighborsClassifier()
rbf.fit(data, targets)
print 'calculated rbf model'
knn.fit(data, targets)
print 'calculated knn model'
# Predict
error_rbf = []
error_knn = []
error_RbfKnn_average=[]
(points, dimensions) = total.shape
for index in range(limitStart+limitLength, limitStart+limitLength+16):
	print index
 	values = total[index, 0:-2]
 	correct = total[index, -1]
 	output_rbf = math.pow((correct - rbf.predict(values)),2)
 	output_knn = math.pow((correct - knn.predict(values)),2)
 	error_rbf.append(output_rbf)
 	error_knn.append(output_knn)
 	error_RbfKnn_average.append((output_rbf+output_knn)/2)
print('Mean Error RBF: ' + str(numpy.mean(error_rbf)))
print('Mean Error KNN: ' + str(numpy.mean(error_knn)))
print('Mean Error AVerage: ' + str(numpy.mean(error_RbfKnn_average)))


#  print('Values: ' + str(values))
#  print('Correct: ' + str(correct))
#  print('RBF: ' + str(output_rbf))
#  print('KNN: ' + str(output_knn))
  


