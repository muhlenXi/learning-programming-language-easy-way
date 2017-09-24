## Head First Python

*mark：up to 76 pages*

Python 提供了一组技术，可以很容易地实现共享，这包括模块和一些发布工具：

- 模块允许你合理组织代码来实现最优共享。
- 发布工具允许你向全世界共享你的模块。

Python 包索引（Python Package Index, PyPI）为 Internet 上的第三方 Python 模块提供了一个集中的存储库。

步骤：

```
python3 setup.py sdist

sudo python3 setup.py install

wine upload dist/mlx_nester-1.0.0.tar.gz

```