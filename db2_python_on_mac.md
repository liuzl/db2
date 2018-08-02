# 在Mac系统安装DB2的python库ibm_db

## 安装
```sh
wget https://files.pythonhosted.org/packages/f8/6f/5f8186cb31021409235a948be5e29d77761ef92747a101360003747c4105/ibm_db-2.0.8.tar.gz
tar -xvzf ibm_db-2.0.8.tar.gz
cd ibm_db-2.0.8 && python setup.py install
```

## 问题

### 问题描述
```python
>>> import ibm_db
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: dlopen(/Users/zliu/anaconda3/lib/python3.6/site-packages/ibm_db-2.0.8-py3.6-macosx-10.7-x86_64.egg/ibm_db.cpython-36m-darwin.so, 2): Library not loaded: libdb2.dylib
  Referenced from: /Users/zliu/anaconda3/lib/python3.6/site-packages/ibm_db-2.0.8-py3.6-macosx-10.7-x86_64.egg/ibm_db.cpython-36m-darwin.so
  Reason: image not found
>>>
```
### 解决方案
1. 将`libdb2.dylib`符号链接到当前目录
    ```
    ln -sf /Users/zliu/anaconda3/lib/python3.6/site-packages/ibm_db-2.0.8-py3.6-macosx-10.7-x86_64.egg/clidriver/lib/libdb2.dylib ./
    ```
2. 修改环境变量`DYLD_LIBRARY_PATH`
    ```
    export DYLD_LIBRARY_PATH=/Users/zliu/anaconda3/lib/python3.6/site-packages/ibm_db-2.0.8-py3.6-macosx-10.7-x86_64.egg/clidriver/lib:$DYLD_LIBRARY_PATH
    ```

## 参考资料
* https://github.com/ibmdb/python-ibmdb/issues/276
* https://www.ibm.com/developerworks/community/blogs/96960515-2ea1-4391-8170-b0515d08e4da/entry/ibm_db_on_MAC_OS_Hints_and_Tips?lang=en
