# Sklearn

## 一.数据集

### 1.加载数据集

`sklearn.datasets`有内置的数据集

import时要注意

- ```python
  >> import sklearn
  >> sklearn.datasets 
  AttributeError: module 'sklearn' has no attribute 'datasets'
  """
  The reason is that the modules inside scikit-learn like datasets are not loaded automatically when loading the top level "sklearn" module. This is to avoid having to load all the modules you do not actually use. Many smaller packages will import their submodules into the top module, and in that case it does not matter
  """
  ```

- ```python
  >> from sklearn import datasets
  ```

```python
iris = datasets.load_iris()
data = iris.data # 2D Array
target = iris.target
```

## 二.训练和预测

### 1.监督学习

**训练：**`fit(X, y)`

**预测：**`predict(T)`

#### 1.1 Nearest neighbor和维度灾难

> 聚类

寻找特征最接近的向量

![../../_images/sphx_glr_plot_classification_001.png](assets\sphx_glr_plot_classification_001.png)

> 维度灾难

为了实现一个有效的聚类，需要让邻近的结点的距离小于设定的某一距离$d$。

- 维度为1时，需要$1/d$个采样点
- 维度为$n$时，需要$1/d^n$个采样点

#### 1.2 Linear model：从回归到稀疏(sparisity)

> Linear regression

$y=X\beta+\epsilon$

<img src="assets\sphx_glr_plot_ols_001.png" alt="../../_images/sphx_glr_plot_ols_001.png" style="zoom:50%;" />

> 特征缩减 shrinkage

防止`over fitting`，让回归系数越小越好，将回归系数纳入`loss`

是`l2`正则化，相较于`l1`长生更多的特征，特征都接近于0

> 稀疏 sparisity化

稀疏就是向量中大部分`index`是`0`

是`l1`正则化，倾向于产生少量的特征，其它特征都是0

#### 1.3 Classification 分类

##### 1.3.1 Logistic Regression

![../../_images/sphx_glr_plot_logistic_001.png](assets\sphx_glr_plot_logistic_001.png)

$y=sigmoid(X\beta-offest)+\epsilon$

```python
>>> log = linear_model.LogisticRegression(C=1e5, penality="")
penalty="l2/l1"
```

##### 1.3.2 Support Vector Machines

找到与两个类别间距最大的超平面

###### 可设置参数

- C：C大时，`over fitting`；C小时，分类效果差

###### 1.3.2.1 SVR Support Vector Regression

用于**回归**

```python
>>> from sklearn import svm
>>> svc = svm.SVR(kernel='linear')
>>> svc.fit(iris_X_train, iris_y_train)
SVR(kernel='linear')
```

###### 1.3.2.2 SVC Support Vector Calssification

用于**分类**

###### 核函数 Kernels

- 'linear'
- 'poly' 多项式
- 'rbf' Radial basis function 径向基函数（高斯径向基函数）

## 三.模型选择

### 1.score， croos-validated score

#### 1.1 score

```python
>>> svc.fit(X_digits[:-100], y_digits[:-100]).score(X_digits[-100:], y_digits[-100:])
0.98
```

#### 1.2 KFold cross-validation

K折交叉验证

将训练集分为K份，其中K-1个用作训练，剩下的一个子集用于验证，循环K次，得到K个模型。

```python
>>> from sklearn.model_selection import KFold, cross_val_score
>>> X = ["a", "a", "a", "b", "b", "c", "c", "c", "c", "c"]
>>> k_fold = KFold(n_splits=5)
>>> for train_indices, test_indices in k_fold.split(X):
...      print('Train: %s | test: %s' % (train_indices, test_indices))
Train: [2 3 4 5 6 7 8 9] | test: [0 1]
Train: [0 1 4 5 6 7 8 9] | test: [2 3]
Train: [0 1 2 3 6 7 8 9] | test: [4 5]
Train: [0 1 2 3 4 5 8 9] | test: [6 7]
Train: [0 1 2 3 4 5 6 7] | test: [8 9]
```

```python
>>> cross_val_score(svc, X_digits, y_digits, cv=k_fold, n_jobs=-1)
array([0.96388889, 0.92222222, 0.9637883 , 0.9637883 , 0.93036212])
```

`n_jods=-1`指调用所有的`CPU`



## 四.约定

### 1.类型转换

如果没有特别说明，输入会被转换为`float64`类型。

**回归**问题的`target`会被转换为`float64`，**分类**问题的`target`不变

### 2.更新超参数

`set_parmas()`

### 3.多分类问题

#### 3.1 使用1d array作为标签

```python
>>> X = [[1, 2], [2, 4], [4, 5], [3, 2], [3, 1]]
>>> y = [0, 0, 1, 1, 2]

>>> classif = OneVsRestClassifier(estimator=SVC(random_state=0))
>>> classif.fit(X, y).predict(X)
array([0, 0, 1, 1, 2])
```

#### 3.2 使用独热编码

```python
>> y = [[0, 1], [0, 2], [1, 3], [0, 2, 3], [2, 4]]
>> y = MultiLabelBinarizer().fit_transform(y)
```

将数据转为独热编码`MulitiLabelBinarizer().fit_transform()`

