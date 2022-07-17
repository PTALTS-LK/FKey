# V1.1用文档
## BOM（物料清单）

[BOM](/HW/Ver1.1/FKey_BOM.txt)

[预览](./Pre.jpg)

## Installing

1.焊接元件到PCB

2.烧录[MicroPython](https://micropython.org/download/esp32/)到ESP32

3.上传主控（Src中的.py文件）

###### 2-3步推荐使用[Thonny IDE](https://github.com/thonny/thonny)完成

## 关于按键宏（AutoPlay）

按键宏储存在一个叫做**play.txt**的文本文件中（以下简称**宏文件**）

由于软件限制，宏文件大小不能太大

文件格式：

五行为一组，从上往下执行

注：切换/松开按键须在下一组同样位置设置成其他键码/0

```
114514  #执行下一组的等待时间以ms为单位
19      #Key1对应键码（键码值具体参见Docs > ch9329串口通讯协议 > 附录）
19      #Key2对应键码
8       #Key3对应键码
10      #Key3对应键码
```

# TO DO
