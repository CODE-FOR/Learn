# HTTP权威指南

## 1. HTTP概述

### 1.3 资源

#### 媒体类型

**MIME类型（MIME type）**：数据格式标签，描述并标记多媒体类型

```
Content type: image/jpeg
```

#### URI

`Uniform Resource Identifier` **统一资源标识符**

一般指URL

- **URL**：统一资源定位符
- *URN：统一资源名

## 2. URL与资源

$URL\rightarrow scheme(http)+://+(host)www.joes-hardware.com+/+(path)index.html$

URL也包括其它组成部分

## 4. 连接管理

### 4.3 HTTP连接的处理

#### 4.3.1 Connection首部

可以存在3中类型的标签：

- HTTP首部字段名：只与此连接有关

  HTTP允许在客户端和源端服务器之间存在一系列HTTP中间实体，例如代理和高速缓存等。所以实际的连接情况有可能是

  ```livescript
  客户端(local) -> 代理（proxy） -> 服务器（remote）
  ```

  如果如图所示的情况：

  <img src="F:\OneDrive\Learn\Web\assests\image-20211217130451385.png" alt="image-20211217130451385" align=left style="zoom:50%;" />

  `Meter`首部选项则只与服务器和代理直接的HTTP连接有关，在代理向客户端发送的首部中应该剔除`Meter`选项，同时也应该剔除`Connection`首部

- 任意标签值：如上例中的`bill-my-credit-card`，有服务器添加的非标准的首部字段

- 值close：操作完成之后需要关闭**持久连接**

#### 4.3.2 串行事务处理时延

<img src="C:\Users\liuzhenwei\AppData\Roaming\Typora\typora-user-images\image-20211217131617989.png" alt="image-20211217131617989" align=left style="zoom:67%;" />

**提升HTTP的连接性能**

- 并行连接：多条TCP连接发起并发HTTP请求
- 持久连接：重用TCP连接，消除连接及关闭时延
- 管道化连接：通过共享的TCP连接发起并发的HTTP请求
- 复用的连接：交替传送请求和响应报文

### 4.4 并行连接

<img src="C:\Users\liuzhenwei\AppData\Roaming\Typora\typora-user-images\image-20211217132819377.png" alt="image-20211217132819377" align=left style="zoom:67%;" />

### 4.5 持久连接

利用的**站点局部性(site locality)**

在事务处理结束之后仍然保持在打开状态的TCP连接被称为持久连接

#### 4.5.2 HTTP/1.0 + keep-alive连接

<img src="C:\Users\liuzhenwei\AppData\Roaming\Typora\typora-user-images\image-20211217133241623.png" alt="image-20211217133241623" align=left style="zoom:67%;" />

#### 4.5.3 keep-alive操作

如果客户端希望为下一条请求将连接保持在打开状态，使用`Connection: Keep-Alive`首部请求。

服务器如果同意，就在`response`中添加`Connection: Keep-Alive`首部，如果不添加，客户端就会关闭连接。

**可能存在的问题，哑代理**

<img src="C:\Users\liuzhenwei\AppData\Roaming\Typora\typora-user-images\image-20211217141236000.png" alt="image-20211217141236000" align=left style="zoom:67%;" />

原因：代理无法理解`Connection: Keep-Alive`，对所有的头部包括`Connection`选项盲目的转发，使得服务器和客户端都错误的认为与对方建立了持久连接，但是代理并没有处理能力，因此等待服务器与其关闭连接，但是服务器认为建立了持久连接，并不关闭与代理的连接，客户端的请求无法到达服务器。

**修正哑代理问题**

使用`Proxy-Connection`首部，代理将`Proxy-Connection`转换为`Connection:Keep-Alive`

<img src="C:\Users\liuzhenwei\AppData\Roaming\Typora\typora-user-images\image-20211217144404679.png" alt="image-20211217144404679" align=left style="zoom:67%;" />

但是只能修复**单个盲中继的问题**

<img src="C:\Users\liuzhenwei\AppData\Roaming\Typora\typora-user-images\image-20211217143543914.png" alt="image-20211217143543914" align=left style="zoom:67%;" />

#### 4.5.8 HTTP/1.1 持久连接

`persistent connection`：默认激活，要关闭需要显示添加`Connection: close`

### 4.6 管道化连接

<img src="C:\Users\liuzhenwei\AppData\Roaming\Typora\typora-user-images\image-20211217151409368.png" alt="image-20211217151409368" align=left style="zoom:67%;" />

### 4.7 关闭连接

**幂等性**：一个事务不管执行一次还是很多次，得到的结果都相同

- GET
- HEAD
- PUT
- DELETE
- TRACE
- OPTIONS

**POST非幂等**

非幂等操作**不可以自动重试**

## 5. Web 服务器

### 5.3 Web服务器的工作

- 建立连接
- 接受请求
- 处理请求
- 访问资源
- 构建相应
- 发送响应
- 记录事务处理过程

### 5.5 接受请求报文

#### 5.5.2 连接的输入/输出处理结构

<img src="C:\Users\liuzhenwei\AppData\Roaming\Typora\typora-user-images\image-20211217212032254.png" alt="image-20211217212032254" align=left style="zoom:67%;" />



## 6. 代理 proxy

### 6.1 代理服务器

<img src="C:\Users\liuzhenwei\AppData\Roaming\Typora\typora-user-images\image-20211213151502083.png" alt="image-20211213151502083" align="left" style="zoom:100%;" />

HTTP代理服务器既是Web`服务器`又是Web`客户端`

### 6.2 代理作用

- 过滤器
- 访问控制
- 防火墙
- Web缓存
- 反向代理
- 内容服务器
- 转码器
- 匿名

#### 正向代理与反向代理

##### 正向代理

对服务器**隐藏真实请求的客户端**

<img src="F:\OneDrive\Learn\Web\assests\v2-07ededff1d415c1fa2db3fd89378eda0_720w.jpg" alt="v2-07ededff1d415c1fa2db3fd89378eda0_720w" style="zoom:80%;" />

客户端**知晓**要访问的服务器，服务器**不知晓**真正发起请求的客户端

##### 反向代理

对客户端**隐藏真实请求的服务器**<img src="F:\OneDrive\Learn\Web\assests\v2-816f7595d80b7ef36bf958764a873cba_720w.jpg" alt="v2-816f7595d80b7ef36bf958764a873cba_720w" style="zoom:80%;" />

客户端**不知晓**实际访问的服务器，代理服务器对最终访问的服务器做了隐藏。

其中可以做**负载均衡**等操作。

### 6.3 代理在何处

#### 代理服务器的部署

- 出口代理：部署在**本地网络的出口点**
- 访问（入口）代理：放在**ISP访问点上**
- 反向代理：部署在**网络边缘，Web服务器之前**
- 网络交换代理：部署在**因特网对等交换点**

<img src="F:\OneDrive\Learn\Web\assests\A9155344F825DB31318B2D85FC5E15A1.png" alt="A9155344F825DB31318B2D85FC5E15A1" style="zoom:50%" align="left" />

#### 代理如何获取流量

- 修改客户端：直接配置**Web客户端**
- 修改网络：**拦截(intercepting)网络流量**导入代理
- 修改DNS的命名空间
- 修改Web服务器：Web服务器向客户端发送HTTP重定向指令，将客户端请求重定向到另一个代理

<img src="F:\OneDrive\Learn\Web\assests\687785D23B9BE8B3E73A2A70D6D22ACE.png" alt="687785D23B9BE8B3E73A2A70D6D22ACE" align=left style="zoom:50%;" />

### 6.4 客户端配置代理

- 手工配置
- **自动配置(Proxy Auto-Configuration PAC)**
- WPAD的代理发现

#### PAC

实际上是`javascript`脚本，是一组规则

```javascript
function FindProxyForURL(url, host) {
  return "DIRECT";
}
```

## 8. 继承点： 网关、隧道及中继

### 8.1 网关

`gateway`，是网关**服务器**，与`default gateway`在ip协议中的网关不同。

可以转化协议。

### 8.5 隧道

**Web 隧道**，解决了原来代理作为**中间人**，需要改写浏览器的请求的问题。将浏览器和远端服务器之间通信的数据**原样传输**，浏览器可以和远端服务器进行TLS握手并传输加密数据。

#### HTTPS以及HTTPS给代理作为中间人带来的问题

> ## HTTPS以及HTTPS给代理作为中间人带来的问题
>
> ### 1. HTTP最大的弊端 不安全
>
> http会**明文**传输信息，没有安全性可言，MD5加密算法安全性也存在缺陷。
>
> ### 2. 加密算法
>
> #### 2.1 对称加密
>
> 加密和解密使用**同一个密钥**，常见的对称加密有DES、3DES和AES。
>
> <img src="F:\OneDrive\Learn\Web\assests\bVbCz9u.png" alt="对称加密数据传输过程" align=left style="zoom:80%;" />
>
> 存在一个**致命**的问题，双方需要使用相同的密钥，在加密传输信息之前，需要协商使用的密钥，需要由一方**明文的传输密钥**给另一方。密钥有可能被截获，因此不够安全。
>
> #### 2.2 非对称加密
>
> 加密和解密使用两个不同的密钥：公钥（public key）和私钥（private key）。公钥和私钥是一对，公钥加密，只有通过私钥才能解密。
>
> <img src="F:\OneDrive\Learn\Web\assests\bVbClUi.png" align=left alt="非对称加密发送 KEY 的过程.png" style="zoom:80%;" />
>
> 最后使用公钥加密生成的密钥KEY，保证了对称加密的密钥KEY的传输安全。
>
> > 非对称加密的计算量大，加密和解密速度相较于对称加密慢很多。所以最后加密传输对称加密的密钥KEY来加速数据传输。
>
> ### 3. HTTPS原理
>
> <img src="F:\OneDrive\Learn\Web\assests\2641864607-5e11d65c74244_fix732.png" alt="2641864607-5e11d65c74244_fix732" align=left style="zoom:80%;" />
>
> **插入：** HTTPS**不加密ip、端口**
>
> ### 4. HTTPS给传统中间人代理模式带来的问题
>
> 由于代理服务器**没有服务器的私钥**，因此代理服务器无法解析客户端**使用服务器公钥**加密传输的数据，也就无法与客户端**建立 TLS连接**，因此传统中间人代理模式失败。
>
> #### 4.1 解决方案一
>
> 让客户端**信任代理服务器的公钥**，代理服务器分别与客户端和远端服务器建立TLS连接。
>
> 例如`flidder`让客户端将`flidder`的证书加入系统认证中以后，可以**抓包分析HTTPS流量**，并且可以将HTTPS流量解析为明文信息。
>
> #### 4.2 解决方案二
>
> 使用**Web隧道**

#### 8.5.1 用CONNECT建立HTTP隧道

`CONNECT`方法请求隧道网关建立一条到达任意目的服务器和端口的**TCP连接**，并对客户端和服务器之间的后续数据进行**盲转发**。

<img src="F:\OneDrive\Learn\Web\assests\image-20211218153150906.png" align=left alt="image-20211218153150906" style="zoom:67%;" />

- 浏览器先**明文**向服务器发送`CONNECT`请求

- 代理服务器接收到**明文**的`CONNECT`请求，解析后与服务器对应端口建立**TCP连接**，建立完成后向客户端发送就绪报文

- 之后网关会盲转发浏览器发送的报文

  > 这样就解决了传统中间人代理模式遇到HTTPS依旧需要需要解析并修改客户端发送的数据的问题。这种通过HTTP隧道承载SSL流量的方式成为**SSL隧道**(SSL隧道是Web隧道的一种)。
  >
  > **SSL隧道与HTTPS的区别：**
  >
  > SSL隧道是Web隧道(Web隧道允许用户通过HTTP连接发送非HTTP流量，这样就可以在HTTP上捎带其他协议数据了)的一种，它经由HTTP连接向默认的80端口发送SSL流量，而HTTPS是经过SSL层加密后向默认的443端口发送加密的HTTP报文。

#### Fiddler 与 HTTPS

> ## Fiddler 与 HTTPS
>
> ### 1. 加入根证书
>
> fiddler会以中间人模式代理
>
> <img src="F:\OneDrive\Learn\Web\assests\20180303002319_70386.png" alt="20180303002319_70386" align=left style="zoom:80%;" />
>
> 为什么会截取**Tunnel to**，也就是HTTP **CONNECT**报文，按道理说使用中间人代理模式并不会使用Web Tunnel，但是依然出现了Tunnel to，而且fiddler可以解析后续的HTTPS报文。
>
> **我的理解**是：
>
> - 系统在识别到使用代理后，对HTTPS协议的报文自动想要建立Web Tunnel，所以发送了HTTP CONNECT报文。
> - fiddler在截取到CONNECT报文后，**并没有按照规定的流程，与服务器建立TCP连接，对后续的通信进行盲转发。**
> - 而是向客户端返回200报文，让客户端认为已经建立好了Web Tunnel，并开始后续的通信。
> - 后续就如上图，fiddler作为中间人处理报文信息。
>
> ### 2. 不加入根证书
>
> 使用**真正的Web Tunnel**模式。

#### python和javascript中的request与代理的关系

> ## python和javascript中的request与代理的关系
>
> ### javascript中的request
>
> javascript中的request默认**不使用系统代理**。
>
> 不论是HTTP流量还是HTTPS流量都要显示的配置proxy。使用fiddler作为辅助工具（监听8888端口）
>
> - 可以正常访问，可以被fiddler抓包
>
>   ```javascript
>   request(
>           {
>               method: 'GET',
>               url: 'http://www.baidu.com',
>               proxy: 'http://localhost:8888'
>           },
>           function (error, response, body) {
>               console.log(error)
>               console.log(response)
>           }
>       )
>   ```
>
> - **可以正常访问**，**不使用系统代理**，不能被fiddler抓包
>
>   ```javascript
>   request(
>           {
>               method: 'GET',
>               url: 'http://www.baidu.com'
>           },
>           function (error, response, body) {
>               console.log(error)
>               console.log(response)
>           }
>       )
>   ```
>
> ### python中的requests
>
> **默认使用系统代理！！！**
>
> **但是HTTPS不显示配置会出bug！！！**
>
> #### HTTP
>
> - 可以正常访问，可以被fiddler抓包，因为**默认使用系统代理**
>
>   ```python
>   response = requests.request('GET', 'https://www.baidu.com', proxies={
>                   'http': 'http://localhost:8888'
>               }, verify=False)
>   ```
>
>   ```python
>   response = requests.request('GET', 'https://www.baidu.com', verify=False)
>   ```
>
> #### HTTPS
>
> - 可以正常访问，不能被fiddler抓包，显示配置https代理为None
>
>   ```python
>   response = requests.request('GET', 'https://www.baidu.com', proxies={
>                   'http': 'http://localhost:8888',
>                   'https': None
>               }, verify=False)
>   ```
>
> - 可以正常访问，可以被fiddler抓包，显示配置https代理
>
>   ```python
>   response = requests.request('GET', 'https://www.baidu.com', proxies={
>                   'http': 'http://localhost:8888',
>                   'https': 'http://localhost:8888'
>               }, verify=False)
>   ```
>
> - 不显示配置https代理，不能正常访问
>
>   ```python
>   response = requests.request('GET', 'https://www.baidu.com', proxies={
>                   'http': 'http://localhost:8888'
>               }, verify=False)
>   ```
>
>   在`request.utils`中的一个函数中
>
>   ```python
>   def select_proxy(url, proxies):
>       """Select a proxy for the url, if applicable.
>   
>       :param url: The url being for the request
>       :param proxies: A dictionary of schemes or schemes and hosts to proxy URLs
>       """
>       proxies = proxies or {}
>       urlparts = urlparse(url)
>       if urlparts.hostname is None:
>           return proxies.get(urlparts.scheme, proxies.get('all'))
>   
>       proxy_keys = [
>           urlparts.scheme + '://' + urlparts.hostname,
>           urlparts.scheme,
>           'all://' + urlparts.hostname,
>           'all',
>       ]
>       proxy = None
>       for proxy_key in proxy_keys:
>           if proxy_key in proxies:
>               proxy = proxies[proxy_key]
>               break
>   
>       return proxy
>   ```
>
>   这种情况最终返回的proxy是http**s**://localhost:8888，，显然是错误的，无法进行正常的请求，因此无法访问，也无法抓包。



