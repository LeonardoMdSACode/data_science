from scipy.spatial.distance import euclidean

plot1 = [1, 3]
plot2 = [2, 5]

distance = euclidean(plot1, plot2)

print("The Euclidean distance between", plot1, "and", plot2, "is", distance)