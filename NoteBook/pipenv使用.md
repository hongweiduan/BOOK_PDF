# pipenv 使用

报错信息：ValueError: unknown locale: UTF-8
```
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
```
- 安装
```
pip install pipenv 
```
- 指定python版本号
```
pipenv --python=python3
```
- 安装requirements
```
pipenv install
```
-  激活虚拟环境
```
pipenv shell
```
- `pipenv graph` 查看目前安装的库及其依赖

