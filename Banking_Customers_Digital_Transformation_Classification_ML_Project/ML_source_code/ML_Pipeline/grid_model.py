from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB # using Gaussian algorithm from Naive Bayes
from sklearn import svm
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import warnings
warnings.simplefilter(action='ignore')


# define a function to perform grid search cv
def grid_model(X_train,y_train,param_grid,model_name):
  model_dict = {
    'logistic_reg' : LogisticRegression,
    'naive_bayes'  : GaussianNB,
    'svm_model'    : svm.SVC,
    'decision_tree': DecisionTreeClassifier,
    'rfcl'         : RandomForestClassifier,
     }

  model = model_dict[model_name]() # any model you want
  model.fit(X_train, y_train)

  grid_search = GridSearchCV(model, param_grid,refit=True,verbose=2)
  grid_search.fit(X_train,y_train)
  final_predictor = grid_search.best_estimator_
  return final_predictor