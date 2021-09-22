# 拉取公共镜像
FROM python:3.6
# 新建工作目录
WORKDIR /weilab
# 将源文件拷贝进工作目录
COPY . /weilab
# 安装使用的相关包
RUN pip install -r requirement.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
# 暴露8080端口
EXPOSE 8080
# 运行程序
CMD ["python", "server.py"]
