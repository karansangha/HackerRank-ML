from sklearn.linear_model import LinearRegression

num_rows = int(input().split()[1])

training_features = list()
training_category = list()

for _ in range(num_rows):
    data = [float(x) for x in input().split()]
    training_category.append(data[-1])
    training_features.append(data[0:-1])

num_tests = int(input())
test_features = list()

for _ in range(num_tests):
    test_features.append([float(x) for x in input().split()])

predictions = LinearRegression().fit(training_features, training_category).predict(test_features)

for prediction in predictions:
    print(prediction)
