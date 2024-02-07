import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline


    # Load your dataset (assume it's in a CSV file)
dataset = pd.read_csv('C:/Users/DELL/Downloads/machine_learning_dataset/spam.csv')

    # Perform data cleaning and preprocessing
dataset['spam'] = dataset['Category'].apply(lambda x: 1 if x == 'spam' else 0)

    # Split the dataset into features (X) and labels (y)
x = dataset["Message"]
y = dataset["spam"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4)

    # Create and fit the pipeline
clf = Pipeline([('vectorizer', CountVectorizer()), ('nb', MultinomialNB())])
clf.fit(x_train, y_train)

    # Print the accuracy on the training and testing sets
train_accuracy = clf.score(x_train, y_train)
test_accuracy = clf.score(x_test, y_test)

    # Save the trained model
joblib.dump(clf, 'spam_model.joblib')


testing_emails = ["don't miss this chance to win 100$ dollars"]
clf.predict(testing_emails)
    # return da
    # return test_accuracy
    


