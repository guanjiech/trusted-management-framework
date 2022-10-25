node.py 

新增一个node节点

set.py

向node节点中set key value

get.py

向node节点中由 key get value

loop.py

循环开启n个node线程

script.py

循环执行set get操作 获得整个kad流程的数据

status.json

保存set的node信息，防止新增未知node节点

test*

不同的value大小



整个kad流程

先loop开启n个node线程 --> 再用script循环执行set get操作，记录耗时