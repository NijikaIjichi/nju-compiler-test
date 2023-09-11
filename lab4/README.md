# compilers-tests

编译原理 Lab4 一键测试脚本。

使用方法：

第一次运行执行 `./run.sh [-r parser] [-e extend] [-l lab] [-ac] [-t timeout]` 

- `parser` 为编译好的`parser`文件的路径（如果在同一路径需要加`./`），注意我们会给你的`parser`传第三个参数，如果你需要利用此脚本测试ir请将ir生成于此参数指示的路径中
- `extend` 为扩展类型（`base`、`extend1`、`extend2`、`both`、`prf`），代表你在lab3中的选做，`prf`还会在`both`上额外测试两个很耗时的样例
- `lab` 可以填`3`或`4`，意为测试ir还是测试mips
- `a` 意为测试advance样例
- `c` 意为遇到错误会直接继续执行不会询问
- `t` 是对单个样例的编译和运行时限，默认30s

之后只需要执行 `./run.sh`。 

注意：测试时会给你的`parser`传第三个参数，建议如果检测到有第三个参数则在其上生成ir，方便debug

由于官方不公布 lab4 的样例，本脚本沿用 lab3 的样例进行测试

## 测试原理

使用了[欧先飞学长用C++写的ir解释器](https://www.github.com/wierton/irsim)。

注意：测试样例的结果由本人的`lab3`在更改除法行为后的`irsim`上运行来生成，已测试过本人的`lab3`在更改除法行为前的`irsim`上运行的结果与标准答案吻合（至于是不是真的是对的就听天由命吧）

做了几处小修改

- 原版在遇到read函数时会打印提示信息(stdout)，对了方便比对输出，该脚本将提示信息删除了
- 在输入结束后，如果IR代码仍然需要read(这通常是由于分支跳转有问题导致的)，则视为runtime error
- irsim在运行时会统计运行的指令数。run.sh在全部运行完后会输出总共运行的指令数（不考虑失败样例）
- **将除法行为更换为C语言中的除法，即向0取整**

会根据test.json里面的信息，将里面的输入作为ir代码解释执行的输入，然后比对ir代码的输出和test.json里面的输出是否吻合

## 添加测试文件

请添加 `test.cmm` 和 `test.json` 两个文件。其中

* `test.cmm` 是源码文件
* `test.json` 是答案描述文件，格式为

```
[
    [input1, output1, ret_val1],
    [input2, output2, ret_val2],
    ...
    [inputk, outputk, ret_valk]
]
```
input和output分别对应输入和输出，也为**列表**，且列表的所有成员均为**整型数**

示例：(tests/naive.json)
```
[
    [[], [2, 0, 1, 7], 0]
]
```
意为，naive.cmm编译成.ir后，仅有一组测试，
该组测试的输入为空，输出为2 0 1 7四个数字。最顶层的main函数应该返回0（由于irsim没有对应接口，它的返回值是解释器的返回值，表示的是解释器是否遇到问题。所以，目前ret_val实际上会被忽略）
