# GitScratchBackend

> ## Warning!
> 此仓库已废弃，对于此仓库的开发将不会得到任何支持。
> 
> **新的支持仓库：[UniScratch/gitscratch-backend-flask](https://github.com/UniScratch/gitscratch-backend-flask)，由Flask构建。**

GitScratch 社区后端。使用 `FastAPI` 构建。

- [GitScratchBackend](#gitscratchbackend)
  - [安装](#安装)
    - [安装依赖](#安装依赖)
    - [启动服务器](#启动服务器)

## 安装

### 安装依赖
``` bash
$ pip3 install fastapi[all]
```

### 启动服务器
``` bash
$ uvicorn app.main:app --reload
```

现在你的服务器将会监听 8000 端口。
