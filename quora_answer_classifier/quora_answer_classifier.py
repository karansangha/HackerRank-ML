from sklearn.ensemble import RandomForestClassifier
import fileinput

training_data = list()
testing_data = list()
n = 0
i = -1
for line in fileinput.input():
    if i == -1:
        n = line.split()[0]

    elif i < int(n):
        training_data.append(line.replace("\n", ""))

    elif i == int(n):
        pass

    else:
        testing_data.append(line.replace("\n", ""))

    i += 1

training_category = list()
training_features = list()

for row in training_data:
    data = row.split()
    training_category.append(int(data[1]))
    training_features.append([float(features.split(":")[1]) for features in data[2:]])

testing_id = list()
testing_features = []

for row in testing_data:
    data = row.split()
    testing_id.append(data[0])
    testing_features.append([float(features.split(":")[1]) for features in data[1:]])

classifier = RandomForestClassifier(n_estimators=50).fit(training_features, training_category)

predictions = classifier.predict(testing_features)

for prediction_id, prediction in zip(testing_id, predictions):
    print('{} {:+}'.format(prediction_id, prediction))
