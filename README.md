# Badge-pattern-printing 徽章图案绘制
This code is used to generate an A4 size PDF that draws all the badges that need to be printed line by line.  

在淘宝上买了自制徽章（吧唧）机，商家给了很多直径70mm的纸片，要画在纸片上才能做。
![image](https://user-images.githubusercontent.com/42110276/170017110-6052fedb-88ba-4287-acb5-d8f9947d085c.png)

打印的图片又不能保证尺寸符合要求。于是诞生了这个用于生成吧唧打印的小脚本，最后可以得到一份可以打印的PDF,打印出来的图案就是需要的大小。

![image](https://user-images.githubusercontent.com/42110276/170016772-1c97450b-21a4-4304-b62d-912039982d80.png)


![image](https://user-images.githubusercontent.com/42110276/170017483-685df94b-e80d-4c59-925d-2eba1684d812.png)

多页：
![image](https://user-images.githubusercontent.com/42110276/170028663-f4ba4be2-4840-4952-8242-f638424e4886.png)

使用的库：
PIL，reportlab

纸张的参数在这里改：
```
paper_h = 279
paper_w = 210
```
和
```
canvas = Canvas('baji.pdf', pagesize=A4)
```

吧唧尺寸的参数在这里改：
```
size = 70  # mm
```

是否使用边框：```draw_frame```变量

是否剪切圆形：```draw_circle```变量


把打印的图片都丢到Images文件夹就行，代码会调整形状大小。

**注意： 实测用A4打出来的话有1-2mm的误差，可以自己调整地大1,2mm，用切圆机切下不影响。**
