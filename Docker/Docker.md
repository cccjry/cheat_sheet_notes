# Docker 簡易操作

## 基本介紹

### 映像檔 Image

> 想像成一個**唯讀**的模板，裏面準備好對應需求的環境設定或是系統。

### 容器 Container

> 透過 Image 所建立的執行實例，通常會有 **啟動**、**開始**、**停止**、**刪除** 等動作，容器之間不互相干擾。

注意到 Image 是唯讀的，容器在啟動的時候建立一層可寫層作為最上層。

### 倉庫 Repository

> Image 集中存放的場所，裡面放著別人完成的 Image。

官方提供的公開倉庫註冊伺服器是 [Docker Hub](https://hub.docker.com/) ，大陸的公開資源則是 [Docker Pool](http://www.dockerpool.com/) ，使用者也可以建立自己的 Repository。其使用概念類似 Git，將製作好的 Image push 上去，在本地端只需要進行pull的動作就好。

### 安裝

直接透過 [官網](https://docs.docker.com/desktop/install/mac-install/) 的說明進行即可。



## 動作

> 底下有出現的指令皆在 MacOS 環境中執行。

### Image 相關

#### 取得 Image

最簡單的管道是 [Docker Hub](https://hub.docker.com/) ，也可以連接到私人倉庫取得。下面的動作表示從預設倉庫(Docker Hub) 拉取(pull) **Ubuntu** ，並且標記為 **22.04**

```
% docker pull ubuntu:22.04
```

#### 列出已知 Image 清單

```
% docker images
REPOSITORY   TAG       IMAGE ID       CREATED       SIZE
ubuntu       22.04     3c2df5585507   2 weeks ago   69.2MB
```

欄位意義：

| REPOSITORY                      | TAG              | IMAGE ID            | CREATED      | VIRTUAL SIZE   |
| ------------------------------- | ---------------- | ------------------- | ------------ | -------------- |
| **來自於哪個倉庫，比如 ubuntu** | **映像檔的標記** | **`ID` 號（唯一）** | **建立時間** | **映像檔大小** |

**TAG** 沒有指定預設為 `latest` ，不過常會使用版本號來做區分，例如 Ubuntu 本身就有很多版本號 `10.04`、`12.04`、`12.10`、`13.04`、`14.04`、`22.04` ... 等等。

#### 建立一個 Image

這個動作類似 `docker pull ubuntu:22.04` ，執行後會立即啟動一個 Container。

```
% docker run -t -i ubuntu:22.04
```

#### 匯出與載入 Image

#### 移除 Image



### Container 相關

#### 用 Image 建立 Container

- 建立但尚未啟動：

```
% docker run --name test ubuntu:22.04 
```

- 建立然後啟動：

```
% docker run --name test ubuntu:22.04 /bin/bash
```

