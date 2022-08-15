# FKey

###### 如果不需要基于本项目修改请不要Frok

##### 如果对本项目硬件/主控有建议或者问题的，欢迎提issues或者discussion

自制4K手台，基于CH9329和esp32开发板，十分简单原理（拓展板式手台）

这个项目是在***完全没有***设计原理图和画PCB的**经验**下进行的

![PRE](/HW/HV1.1/PCB_PCB_Fkey_2022-06-02.svg)


## 项目文件结构

**[HW](/HW)** 存放硬件原理图/PCB和GerBer生产文件

**[Src](/Src)** 存放MicroPython主控程序

**[Docs](/Docs)** 存放各种文档

## 功能/计划
 - [x] 基本键位映射(DFJK,可在主控自行更改)
 - [x] 外接按键/开关(HV1.1)
 - [x] 外接电源(HV1.1)
 - [x] 按键背光(HV1.1)
 - [x] AutoPlay(按键宏)(HV1.1,SV1.1-AutoPlay)

 - [ ] BLE Keyboard
 - [ ] And More .......

## 版权声明
本项目使用GPLv3协议
```
Fkey
Copyright (C) 2022 PCX-LK

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
```
