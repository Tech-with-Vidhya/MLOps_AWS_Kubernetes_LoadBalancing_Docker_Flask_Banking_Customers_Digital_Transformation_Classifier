from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB # using Gaussian algorithm from Naive Bayes
from sklearn import svm
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from ML_Pipeline.utils import max_val_index
from ML_Pipeline.model_evaluation import evaluate_model
import warnings
warnings.simplefilter(action='ignore')

# create a function to train all the models
def train_model(X_train,y_train,X_test,y_test):
     model_dict = {
         'logistic_reg' : LogisticRegression(solver="liblinear"),
         'naive_bayes'  : GaussianNB(),
         'svm_model'    : svm.SVC(gamma=0.25, C=10),
         'decision_tree': DecisionTreeClassifier(criterion = 'gini', max_depth = 5, random_state=1),
         'rfcl'         : RandomForestClassifier(random_state=1),
     }
     fitted_model=[] 
     score=[] # for accuracy score


     for model_name in list(model_dict.keys()):   
        model = model_dict[model_name]
        fitted_model.append(model.fit(X_train, y_train))
        score.append(evaluate_model(y_test, model.predict(X_test), 'accuracy_score'))
        
     max_test = max_val_index(score) # for maximum accuracy amongst all the models trained
     max_score = max_test[0]
     max_score_index = max_test[1]
     final_model = fitted_model[max_score_index]
     return (final_model, max_score) # returns the best model with highest accuracy value
