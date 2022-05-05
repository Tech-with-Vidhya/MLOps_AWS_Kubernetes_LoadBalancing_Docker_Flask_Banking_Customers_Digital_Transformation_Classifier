from sklearn import metrics
from sklearn.metrics import accuracy_score

# function to calculate the accuracy score of a model
def evaluate_model(y_test, y_pred, method):
    if method =='accuracy_score':
        score= accuracy_score(y_test, y_pred)
    else: 
        print("Only available acuuracy measures is mae.")
    return score


# similarly you create these metrics for precision and recall as well and use them instead
