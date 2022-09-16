# 写在前面
&emsp;&emsp;各式资料中关于BP神经网络的讲解已经足够全面详尽，故不在此过多赘述。本文重点在于由一个“最简单”的神经网络练习推导其训练过程，和大家一起在练习中一起更好理解神经网络训练过程。
# 一、BP神经网络
## 1.1 简介

&emsp;&emsp;BP网络（Back-Propagation Network） 是1986年被提出的，是一种按误差逆向传播算法训练的
&emsp;&emsp;多层前馈网络，是目前应用最广泛的神经网络模型之一，用于函数逼近、模型识别分类、数据压缩和时间序列预测等。
&emsp;&emsp;一个典型的BP网络应该包括三层:输入层、隐藏层和输出层。各层之间全连接，同层之间无连接。隐藏层可以有很多层。
![Fig 1 数字图像与对应矩阵图示](https://img2022.cnblogs.com/blog/2745075/202202/2745075-20220221145545646-373687976.png "Fig 1 数字图像与对应矩阵图示")
<center>Fig 1 数字图像与对应矩阵图示</center>
<br></br>

## 1.2 训练(学习)过程
&emsp;&emsp;每一次迭代(Interation)意味着使用一批(Batch)数据对模型进行一次更新过程，被称为“一次训练”，包含一个正向过程和一个反向过程。
具体过程可以概括为如下过程：
<ol>
<li>准备样本信息(数据&标签)、定义神经网络(结构、初始化参数、选取激活函数等)</li>
<li>将样本输入，正向计算各节点函数输出</li>
<li>计算损失函数</li>
<li>求损失函数对各权重的偏导数，采用适当方法进行反向过程优化</li>
<li>重复2~4直至达到停止条件</li>
</ol>
&emsp;&emsp;<font color="red"><strong>以下训练将使用均值平方差（Mean Squared Error， MSE）作为损失函数，sigmoid函数作为激活函数、梯度下降法作为优化权重方法进行推导</strong></font>

# 二、实例推导练习作业
## 2.1 准备工作
![Fig 2 所定义神经网络、初始化参数、样本信息等](https://img2022.cnblogs.com/blog/2745075/202202/2745075-20220221150513757-568980169.png "Fig 2 所定义神经网络、初始化参数、样本信息等")
<center>Fig 2 所定义神经网络、初始化参数、样本信息等 </center>
<br></br>
<ol>
<li>第一层是输入层，包含两个神经元： i1， i2 和偏置b1</li>
<li>第二层是隐藏层，包含两个神经元： h1， h2 和偏置项b2</li>
<li>第三层是输出： o1， o2</li>
<li>每条线上标的 wi 是层与层之间连接的权重</li>
<li>激活函数是 sigmod 函数</li>
<li>我们用 z 表示某神经元的加权输入和，用 a 表示某神经元的输出</li>
</ol>

## 2.2 第一次正向过程【个人推导】
&emsp;&emsp;根据上述信息，我们可以得到另一种表达一次迭代的“环形”过程的图示如下：
![Fig 3 bp神经网络数量关系“环”图示](https://img2022.cnblogs.com/blog/2745075/202202/2745075-20220221150853293-699179322.png "Fig 3 bp神经网络数量关系“环”图示")
<center>Fig 3 bp神经网络数量关系“环”图示  </center>
<br></br>
&emsp;&emsp;我们做一次正向过程(由于需多次迭代，因此我们将第一次正向过程标记为t=0)，得各项数值如下：

![Fig 4 初始数值“环”图示(附函数关系表达式)](https://img2022.cnblogs.com/blog/2745075/202202/2745075-20220221151353005-1483291791.png "Fig 4 初始数值“环”图示(附函数关系表达式)")
<center>Fig 4 初始数值“环”图示(附函数关系表达式)</center>
<br>
&emsp;&emsp;由此我们可得损失函数值为MSE=0.298371109，假设这超出了我们对损失值的要求，那么我们就需要对各个权重(wi,t=0)进行更新， 作为t=1的初始权重。

## 2.3 推导计算∂/∂wi【个人推导】
### 2.3.1 均值平方差损失函数的全微分推导

![1663309414706](https://user-images.githubusercontent.com/92873873/190570645-f8d49801-6878-4298-a652-fb850281bcc3.png)

### 2.3.2 这一次代入训练实例的数值和各数量名

![1663309530651](https://user-images.githubusercontent.com/92873873/190570945-30b174a1-84b8-46b4-8095-ab10b6545b4e.png)

### 2.3.3 由此我们得到 $∂/∂wi$ 的表达式
$\frac {\partial MSE}{\partial \omega_{1}}=-\left [ \left( y_{1}-ao_{1} \right )ao_{1}\left ( 1-ao_{1} \right )\cdot \omega_{5}+\left( y_{2}-ao_{2} \right )ao_{2}\left ( 1-ao_{2} \right )\cdot \omega_{7}\right ]\cdot ah_{1}\left ( 1-ah_{1} \right ) \cdot i_{1}$
$\frac {\partial MSE}{\partial \omega_{2}}=-\left [ \left( y_{1}-ao_{1} \right )ao_{1}\left ( 1-ao_{1} \right )\cdot \omega_{5}+\left( y_{2}-ao_{2} \right )ao_{2}\left ( 1-ao_{2} \right )\cdot \omega_{7} \right ]\cdot ah_{1}\left ( 1-ah_{1} \right )\cdot i_{2}$
$\frac {\partial MSE}{\partial \omega_{3}}=-\left [ \left( y_{1}-ao_{1} \right )ao_{1}\left ( 1-ao_{1} \right )\cdot \omega_{6}+\left( y_{2}-ao_{2} \right )ao_{2}\left ( 1-ao_{2} \right )\cdot \omega_{8} \right ]\cdot ah_{2}\left ( 1-ah_{2} \right )\cdot i_{1}$
$\frac {\partial MSE}{\partial \omega_{4}}=-\left [ \left( y_{1}-ao_{1} \right )ao_{1}\left ( 1-ao_{1} \right )\cdot \omega_{6}+\left( y_{2}-ao_{2} \right )ao_{2}\left ( 1-ao_{2} \right )\cdot \omega_{8} \right ]\cdot ah_{2}\left ( 1-ah_{2} \right )\cdot i_{2}$
$\frac {\partial MSE}{\partial \omega_{5}}=-\left( y_{1}-ao_{1} \right )ao_{1}\left ( 1-ao_{1} \right )\cdot ah_{1}$
$\frac {\partial MSE}{\partial \omega_{6}}=-\left( y_{1}-ao_{1} \right )ao_{1}\left ( 1-ao_{1} \right )\cdot ah_{2}$
$\frac {\partial MSE}{\partial \omega_{7}}=-\left( y_{2}-ao_{2} \right )ao_{2}\left ( 1-ao_{2} \right )\cdot ah_{1}$
$\frac {\partial MSE}{\partial \omega_{8}}=-\left( y_{2}-ao_{2} \right )ao_{2}\left ( 1-ao_{2} \right )\cdot ah_{2}$
<br>&emsp;&emsp;当然如果你喜欢用矩阵表示也可以：
(P.S. Markdown编辑器承受不住如此“巨大”的矩阵算式而崩溃，我只好转成svg图片贴上了，见谅~)</br>
![image](https://user-images.githubusercontent.com/92873873/190571253-1f4b31ab-84e4-42a6-92d0-29a9ed5f030d.png)

![image](https://user-images.githubusercontent.com/92873873/190571275-2383ffb7-9963-420b-a44f-8b6d287da7c6.png)

【2022.06.06 update】
![1663309750293](https://user-images.githubusercontent.com/92873873/190571474-0788d2b3-bf23-4df8-bd67-eb766036ed55.png)

&emsp;&emsp;**相较于之前的矩阵化分解而言，新的矩阵表示更有利于编程的代码实现。**

## 2.4 根据∂/∂wi梯度下降法优化wi【个人推导】
&emsp;&emsp;根据梯度下降法 ${\color{purple}{\omega_{i,t+1}=\omega_{i,t}+\alpha_{t}\left [ -\triangledown Loss(\omega_{i,t}) \right ]}}$ ，设置学习率α=0.5，计算出wi,t+1，然后重新进行下一次正向过程。(可以将该过程在Excel中轻易实现，下表中为迭代数据截取)
&emsp;&emsp;可以看到，经过10001次迭代之后MSE(t=10001)=3.51019E-05已经足够小，可以停止迭代完成1代训练。

![image](https://img2022.cnblogs.com/blog/2745075/202202/2745075-20220221190014513-2028348689.png)
………………………………………………………………………………………………………………………………………………
![image](https://img2022.cnblogs.com/blog/2745075/202202/2745075-20220221190225988-430575907.png)

# sigmoid函数求导Tips(for于初级选手)
![1663309839569](https://user-images.githubusercontent.com/92873873/190571711-2147f889-b347-4b1d-87e7-bc3e4fd5333b.png)
