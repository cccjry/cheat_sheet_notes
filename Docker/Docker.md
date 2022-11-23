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

##### 從 Docker Hub 直接拉取

這個動作與 `docker pull ubuntu:22.04` 同樣都會建立 Image，執行後會立即啟動一個 Container。

```
% docker run --name JerryDocker -t -i ubuntu:22.04
root@835283f29768:/#
root@835283f29768:/# apt-get update
root@835283f29768:/# apt-get install sudo
root@835283f29768:/# exit
```

##### 變更後重新提交新的副本

變更內容 (以簡單安裝動作為例) 後離開 Container ，接著可以透過 `docker commit` 提交變更後的副本，成為另一個新的 Image。成功則會印出新的 Image 的 **`ID`** 。

```
% docker commit -m "install sudo" -a "Jerry" 835283f29768 test:JerryDocker
sha256:ad4fbed3d7a30239b9471acc027984f169c4cba5b58f254caa998ae86532c6b0
% docker images
REPOSITORY   TAG       IMAGE ID       CREATED              SIZE
test         JerryDocker   ad4fbed3d7a3   18 seconds ago   109MB	<-----
ubuntu       22.04         3c2df5585507   2 weeks ago      69.2MB
```

##### 利用 Dockerfile 建立 Image

範例 (此內容建立出來的 Image 與上方範例一摸一樣)：

```
# Comment
From ubuntu:22.04
MAINTAINER Docker Jerry <test@gmail.com>
RUN apt-get update
RUN apt-get install sudo
```

Dockerfile 基本的語法是

- 使用`#`來註釋
- `FROM` 指令告訴 Docker 使用哪個映像檔作為基底
- 接著是維護者的信息
- `RUN`開頭的指令會在建立中執行，這邊使用 apt-get 來安裝了一些套件

```
% docker build - < Dockerfile -t 'test2:JerryDocker'
[+] Building 13.2s (7/7) FINISHED                                                                                                                       
 => [internal] load build definition from Dockerfile
 => => transferring dockerfile: 191B
 => [internal] load .dockerignore
 => => transferring context: 2B
 => [internal] load metadata for docker.io/library/ubuntu:22.04
 => [1/3] FROM docker.io/library/ubuntu:22.04
 => [2/3] RUN apt-get update
 => [3/3] RUN apt-get install sudo
 => exporting to image
 => => exporting layers
 => => writing image sha256:4fdf18202b0885bf4c83d3d3c77144eb1454c1c2deafa49e80ff85852ca9980b
 => => naming to docker.io/library/test2:JerryDocker 
% docker images
REPOSITORY   TAG           IMAGE ID       CREATED          SIZE
test2        JerryDocker   4fdf18202b08   4 minutes ago    109MB	<-----
test         JerryDocker   ad4fbed3d7a3   11 minutes ago   109MB
ubuntu       22.04         3c2df5585507   2 weeks ago      69.2MB
```

可以看到每一個動作都是在 Dockerfile當中所定義好的，完成後同樣會印出新的 Image 的 **`ID`** 。

另外可以用 `docker tag [ID] [name:tag]` 複製出一個 **相同 `ID`** 的 Image。

```
% docker tag 4fdf18202b08 test2:JerryDocker2
% docker images                             
REPOSITORY   TAG            IMAGE ID       CREATED          SIZE
test2        JerryDocker    4fdf18202b08   10 minutes ago   109MB
test2        JerryDocker2   4fdf18202b08   10 minutes ago   109MB	<-----
test         JerryDocker    ad4fbed3d7a3   18 minutes ago   109MB
ubuntu       22.04          3c2df5585507   2 weeks ago      69.2MB
```

##### 從檔案建立

詳見 [docker import](https://docs.docker.com/engine/reference/commandline/import/) 。

#### 匯出與載入 Image

##### 匯出

```
% docker save -o test2.tar test2:JerryDocker2
```

##### 載入

```
% docker load --input test2.tar
```

#### 移除 Image

以下幾種方式都可以：

- `docker rmi [name:tag]`
- `docker rmi [ID]`

**NOTE**: 若 `ID` 有對應到多個 `name:tag` ，可以加上 `-f` 強制將同一個 `ID` 全部刪除；或是手動針對 `name:tag` 刪除。

[更多請看這裡](https://docs.docker.com/engine/reference/commandline/rmi/)



### Container 相關

#### 用 Image 建立 Container （啟動）

- 建立但尚未啟動：

```
% docker run --name test ubuntu:22.04 
```

- 建立然後啟動：

```
% docker run --name test ubuntu:22.04 /bin/bash
```

#### 後台執行（守護態執行）

#### 終止

#### 進入容器

#### 匯出與載入 Container

#### 刪除
