# GitScratchBackend
GitScratch社区的后端部分，处理GitScratchFrontend的请求。使用`FastAPI`构建。

## Install/安装

### Install requirements/安装依赖
```bash
$ pip3 install fastapi[all]
```
### Start server/启动服务器
```bash
$ uvicorn app.main:app --reload
```

现在你的服务器将会监听8000端口
Then your server will listen port 8000.