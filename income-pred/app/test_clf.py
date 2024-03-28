import pickle
from sklearn.metrics import f1_score

# Load the model
with open("income.pkl", "rb") as f:
    clf = pickle.load(f)

def test_f1_score():
    # Load test data
    with open("data/test_data.pkl", "rb") as file:
        test_data = pickle.load(file)

    # Unpack the tuple
    X_test, y_test = test_data

    # convert to int as it is in float
    y_test = y_test.astype(int)

    # Predict on test data
    y_pred = clf.predict(X_test)

    # Compute f1_score of classifier
    f_score = f1_score(y_test, y_pred)

    # f1_score should be over 67%
    assert f_score > 0.675

