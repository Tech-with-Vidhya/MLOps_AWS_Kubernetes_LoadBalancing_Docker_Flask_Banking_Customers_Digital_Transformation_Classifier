#importing required packages
import pickle
from sklearn.model_selection import train_test_split
from ML_Pipeline.utils import read_data, merge_dataset,drop_col, null_values
from ML_Pipeline.train_model import train_model
from ML_Pipeline.grid_model import grid_model
# import imblearn
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler
from imblearn.pipeline import Pipeline
from collections import Counter
from scipy.stats import zscore


# Read the initial datasets
data1 = read_data("../input/Data1.csv")
data2 = read_data("../input/Data2.csv")

# Merge the two datasets
final_data = merge_dataset(data1,data2,join_type='inner',on_param = 'ID')

# drop columns 
final_data = drop_col(final_data,['ID','ZipCode','Age'])

# drop null values
final_data = null_values(final_data)

# Train-test split - Perform train-test split on the data, 75-25 split - on imbalanced data
x_train, x_test, y_train, y_test = train_test_split(final_data.drop(['LoanOnCard'],axis=1),
                                                    final_data['LoanOnCard'],
                                                    test_size = 0.3,
                                                    random_state = 1 )
# model = train_model(x_train, y_train, x_test, y_test) - train the model on imbalanced data


### In order to balance the data ###

# convert all attributes to Z scale
XScaled  = final_data.drop(['LoanOnCard'],axis=1).apply(zscore)   

# summarize class distribution
counter = Counter(final_data['LoanOnCard'])

# define pipeline
over = SMOTE(sampling_strategy=0.3,random_state=1) #sampling_strategy=0.1,random_state=1
under = RandomUnderSampler(sampling_strategy=0.5)
steps = [ ('o', over),('u', under)]
pipeline = Pipeline(steps=steps)

# transform the dataset
Xb, Yb = pipeline.fit_resample(XScaled, final_data['LoanOnCard'])

# summarize the new class distribution
counter = Counter(Yb)

# split the balanced data into train and test
x_trainb, x_testb, y_trainb, y_testb = train_test_split(Xb, Yb, test_size=0.3, random_state=1)


# chosing hyperparameter using Grid Search
# Using GridSearchCV for tuning the required model(in this case we are using GridsearchCV on svm)
# (This can be performed for any model by changing the param_grid accordingly)
param_grid = {'C': [0.1,1, 10, 100],
              'gamma': [1,0.1,0.25,0.01],
              'kernel': ['rbf', 'poly', 'sigmoid']}

model_grid_search = grid_model(x_trainb,y_trainb, param_grid,'svm_model') 
print(model_grid_search)


# train the model
model = train_model(x_trainb, y_trainb, x_testb, y_testb)
print(model)
pickle.dump(model, open('../output/finalized_model.sav','wb'))
