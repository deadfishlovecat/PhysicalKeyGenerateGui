# PhysicalKeyGenerateGui
物理层密钥的上位机的算法实现以及最后的图形化界面的实现

## 代码架构
```
.
+-- README.md                                                             % 当前文档
+-- .gitignore                                                                                                                            
+-- KeyGenerate                                                           % 密钥算法的生成                        
|   +-- dealData.py                                                          % 密钥算法的主体
|   +-- draw.py                                                              % 一些绘图函数
|   +-- Error_correction.py                                                  % 使用74汉明编码进行编码
|   +-- main.py                                                              % 对整体的算法流程进行测试
```
