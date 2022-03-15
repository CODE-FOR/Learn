# Pandas

## 1. Series

`表`中的一`列`，''一维''数组，数组里的内容不一定是原子变量

```python
>>> a = [1, 7, 2]
>>> f = pd.Series(a)
>>> f[0]
... 1
>>> f = pd.Series(a, index=['x', 'y', 'z'])
>>> f['x']
... 1
```

可以直接用`dict`初始化，`index`的作用是筛选标签

```python
>>> calories = {"day1": 420, "day2": 380, "day3": 390}
>>> myvar = pd.Series(calories, index = ["day1", "day2"])
>>> myvar
... day1    420
... day2    380
... dtype: int64
```

| index |      |
| ----- | ---- |
| day1  | 420  |
| day2  | 380  |

## 2. DataFrame

### 2.1 初始化

整个`表格`，''二维''数组，数组里的内容不一定是原子变量

```python
>>> data = {
...   "calories": [420, 380, 390],
...   "duration": [50, 40, 45]
... }
>>> df = pd.DataFrame(data)
>>> df
...      calories  duration
...   0       420        50
...   1       380        40
...   2       390        45
>>> df = pd.DataFrame(data, index=['a', 'b', 'c'])
...      calories  duration
...   a       420        50
...   b       380        40
...   c       390        45
```

| index | calories | duration |
| ----- | -------- | -------- |
| a     | 420      | 50       |
| b     | 380      | 40       |
| c     | 390      | 45       |

### 2.2 返回行列

#### 2.2.1 返回行

`df.loc[]`可以返回特定行或特定**多**行，**使用index或index数组**

##### 返回特定行

```python
>>> df.loc[0]
...   calories    420
...   duration     50
...   Name: 0, dtype: int64
```

返回的是**Series**

##### 返回特定多行

```python
>>> df.loc[[0, 1]]
...      calories  duration
...   0       420        50
...   1       380        40
```

返回的是**DataFrame**

#### 2.2.2 返回特定元素

```python
>>> df.loc[0, 'calories']
... 420
```

### 2.3 加载文件

#### 2.3.1 CSV

```python
>>> df = pd.read_csv('data.csv')
```

设置展示的最大行数

```python
>>> pd.options.display.max_rows = 9999
```

## 3. 分析处理数据

前n行：`df.head(n)`

后n行：`df.tail(n)`

信息：`df.info()`

### 3.1 清洗数据

#### 3.1.1 处理空数据

##### 去除空数据

```python
>>> df.dropna(inplace=True)
```

##### 替换空数据

```python
>>> df.fillna(130, inplace = True)
```

##### 处理特定列

```python
>>> df["Calories"].fillna(130, inplace = True)
```

#### 3.1.2 删除行

利用`index`输出行

```python
>>> df.drop(0, inplace=True)
```

#### 3.1.3 处理重复数据

##### 查看是否有重复数据

```python
>>> df.duplicated()
... True
```

##### 去除重复数据

```python
>>> df.drop_duplicates(inplace = True)
```

### 3.2 数据相关性分析

```python
>>> df.corr()
...             Duration     Pulse  Maxpulse  Calories
...   Duration  1.000000 -0.155408  0.009403  0.922721
...   Pulse    -0.155408  1.000000  0.786535  0.025120
...   Maxpulse  0.009403  0.786535  1.000000  0.203814
...   Calories  0.922721  0.025120  0.203814  1.000000
```

忽略非`numeric`的列

至少$0.6$或$-0.6$才能认为存在较好的相关性