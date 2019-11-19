### 引入第三方代码的三种方式

1、`import module_name`

```python
import math

print(math.gcd(4, 6)) # 2
```

2、给 module 起别名

```python
import math as m

m.gcd(4, 6)
```

3、使用 from 引入名称

```python
from math import gcd, sqrt
from math import * # 不推荐使用，避免被意外覆盖

sqrt(gcd(4, 6))
```

