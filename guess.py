import sys, datetime, numpy, math
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
dataset = sys.argv[1] #the .csv file we are reading form
limitStart= int(sys.argv[2]) #the first data point we are looking at
limitLength = int(sys.argv[3]) # how many subsequent datpoint we should look at

def createData(hr):
	return total[limitStart:(limitStart+limitLength-hr), 0:-1]
def createTargets(hr):
	return total[(limitStart+hr):limitStart+limitLength, -1]

# Import dataset
total = numpy.genfromtxt(dataset, delimiter=',')
with open('predictions.csv', 'w') as predictions:
	for hour in range(1,16):
		data = createData(hour)
		targets = createTargets(hour)

		# Train
		rbf = svm.SVC(kernel='rbf')
		knn = KNeighborsClassifier()
		rbf.fit(data, targets)
		knn.fit(data, targets)

		#predict
		lastDataPoint = total[limitStart+limitLength, 0:-1]
		predict = knn.predict(lastDataPoint)
		predictions.write(str(predict[0])+'\n')

# Predict
# error_rbf = []
# error_knn = []
# (points, dimensions) = total.shape
# for index in range(limitStart+limitLength, limitStart+limitLength+16):
#  	values = total[index, 0:-1]
#  	correct = total[index+hour, -1]
#  	output_rbf = math.pow((correct - rbf.predict(values)),2)
#  	output_knn = math.pow((correct - knn.predict(values)),2)
#  	error_rbf.append(output_rbf)
#  	error_knn.append(output_knn)
# print('Mean Error RBF: ' + str(numpy.mean(error_rbf)))
# print('Mean Error KNN: ' + str(numpy.mean(error_knn)))
  





