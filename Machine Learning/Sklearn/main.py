from sklearn import datasets
import sklearn
from sklearn import svm
import pandas
from sklearn.model_selection import KFold, cross_val_score, ShuffleSplit

user_feature_and_label = pandas.read_json('user_feature.log')
user_feature = user_feature_and_label[['same_post_user', 'same_comments_user_in_down_comments_user', 'same_comments_user_in_up_comments_user']]
user_label = user_feature_and_label['label']

svm_model = svm.SVC(C=1e-1)
k_fold = ShuffleSplit(n_splits=5, test_size=.25, random_state=0)
print(cross_val_score(svm_model, user_feature, user_label, cv=k_fold, n_jobs=-1, scoring='f1'))