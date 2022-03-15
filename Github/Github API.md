### 获取分页项目的总页数

例如想要获取一个项目的`commits`数量，如果遍历寻找每一页则开销过大，因此需要寻找到总页数。

在`response headers`中会蕴含总页数信息。

例如使用

```python
response = requests.request('GET', 'api.github.com/repos/numpy/numpy/commits?per_page=100&page=1', 
                            headers={
                                    	'Authorization': 'token ' + token
                            })
```

得到的`headers`

```json
Status: 200 OK
Link: <https://api.github.com/resource?page=2>; rel="next",
      <https://api.github.com/resource?page=5>; rel="last"
X-RateLimit-Limit: 5000
X-RateLimit-Remaining: 4999
```

如果存在`Link`项则说明存在下一页以及会标注出最后一页`rel=last`

因此可以使用正则找到`last_page_num`

```python
link = response.headers.get('link', None)
if link is not None:
    total_page_num = int(re.findall('&page=[0-9]+', response.headers['link'].split(',')[1])[0].split('=')[1])
```

