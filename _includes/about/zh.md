<style>
.post-container img[alt=badge] {
    display: inline;
    max-width: 100%;
    height: auto;
    margin: auto auto auto auto;
}

.post-container a img:hover, a img[alt=badge]:focus{
    cursor: pointer;
}
</style>

> 说点什么

##### 教育经历

* 2014 - 2018 &nbsp;&nbsp; 哈尔滨工业大学 &nbsp;&nbsp; **学士学位**
  * 培养单位：[计算机科学与技术学院](http://www.cs.hit.edu.cn/)
  * 专业：物联网工程

* 2018 - 2021 &nbsp;&nbsp; 中国科学院大学 &nbsp;&nbsp; **硕士学位**
  * 校级培养单位：[人工智能学院](https://ai.ucas.ac.cn/index.php/zh-cn/)
  * 所级培养单位：[中国科学院计算技术研究所](http://www.ict.cas.cn/)
  * 专业：计算机技术

##### 技术栈

##### 开源项目

###### Virtual Idol Sharing Project - OpenVtuber

![BVmyWt.gif](https://s1.ax1x.com/2020/10/24/BVmyWt.gif)

![badge](https://badgen.net/github/stars/1996scarlet/OpenVtuber?icon=github&color=cyan&scale=1)
![badge](https://badgen.net/github/forks/1996scarlet/OpenVtuber?icon=git&color=orange&scale=1)
![badge](https://badgen.net/github/open-issues/1996scarlet/OpenVtuber?icon=circleci&color=yellow&scale=1)
![badge](https://badgen.net/github/release/1996scarlet/OpenVtuber/stable?icon=docker&color=green&scale=1)

虚拟爱抖露(アイドル)共享计划, 是基于单目RGB摄像头的人眼与人脸特征点检测算法, 在实时3D面部捕捉以及模型驱动领域的应用.

将该年度ICCV/ECCV/CVPR中的SOTA算法复现并更新

在2019年发布的版本中, 我们采用改进的Faster Retina Face作为人脸检测器, 采用

---

###### ArcFace Based Real-Time Facial Recognition System

![ArcFace Demo](/img/github_repo/ArcFace_Multiplex_Recognition.webp)

![badge](https://badgen.net/github/stars/1996scarlet/ArcFace-Multiplex-Recognition?icon=github&color=cyan&scale=1)
![badge](https://badgen.net/github/forks/1996scarlet/ArcFace-Multiplex-Recognition?icon=git&color=orange&scale=1)
![badge](https://badgen.net/github/open-issues/1996scarlet/ArcFace-Multiplex-Recognition?icon=circleci&color=yellow&scale=1)
![badge](https://badgen.net/github/release/1996scarlet/ArcFace-Multiplex-Recognition/stable?icon=docker&color=green&scale=1)

---

###### [Faster Mobile Retina-Face](https://github.com/1996scarlet/faster-mobile-retinaface)

![FMRF](https://s1.ax1x.com/2020/10/24/BVzKvn.jpg)

[![badge](https://badgen.net/github/stars/1996scarlet/faster-mobile-retinaface?icon=github&color=cyan&scale=1)](https://github.com/1996scarlet/faster-mobile-retinaface/stargazers)
[![badge](https://badgen.net/github/forks/1996scarlet/faster-mobile-retinaface?icon=git&color=orange&scale=1)](https://github.com/1996scarlet/faster-mobile-retinaface/network/members)
[![badge](https://badgen.net/github/open-issues/1996scarlet/faster-mobile-retinaface?icon=circleci&color=yellow&scale=1)](https://github.com/1996scarlet/faster-mobile-retinaface/issues)
[![badge](https://badgen.net/github/release/1996scarlet/faster-mobile-retinaface/stable?icon=docker&color=green&scale=1)](https://github.com/1996scarlet/faster-mobile-retinaface/releases)

[RetinaFace(CVPR 2020)](https://openaccess.thecvf.com/content_CVPR_2020/html/Deng_RetinaFace_Single-Shot_Multi-Level_Face_Localisation_in_the_Wild_CVPR_2020_paper.html)是Single-Shot人脸检测的代表工作, 以平面像素点回归为核心思想, 将人脸定位、特征点标记、边框回归等任务集成在单个网络中. 尽管RetinaFace是目前State of the Art的人脸检测器, 但复杂的网络结构却导致其无法有效地运行在低功耗设备中.

为此, 我们以[MobileNetV2](https://openaccess.thecvf.com/content_cvpr_2018/html/Sandler_MobileNetV2_Inverted_Residuals_CVPR_2018_paper.html)为主干, 在RetinaFace框架的基础上进行多项改进, 实现了轻量级、高精度的Faster Mobile Retina-Face(FMRF). 在网络结构方面, 通过适当削减FPN层数并降低锚框密度而减少了不必要的特征提取与分类; 特征点检测分支的移除也显著提升了模型的推断效率. 此外, FMRF还对框架的实现细节进行了优化. 在预处理阶段, 通过直接调用底层接口以绕开多余的格式校验; 在推断过程中则通过缓存Runtime Anchors避免了重复计算; 而针对[NMS](https://www.paperswithcode.com/method/non-maximum-suppression)算法的向量化改进也显著降低了后处理阶段的耗时.

在公开数据集[WIDER FACE](http://shuoyang1213.me/WIDERFACE/)上的实验结果表明, 我们的方法能够在保持同等精度的前提下, 取得最高32%的速度提升, 并占用更少的内存与显存资源.

---

##### 文章与专利

###### A Backbone Replaceable Fine-tuning Network for Stable Face Alignment

Xu Sun, Yingjie Guo, Shihong Xia*

CoRR abs/2010.09501 (2020)

[Paper](https://arxiv.org/abs/2010.09501)&nbsp;&nbsp;\|&nbsp;
[Video](https://www.bilibili.com/video/BV1Pa4y1J7tU)&nbsp;&nbsp;\|&nbsp;
[Code](https://github.com/1996scarlet/OpenVtuber)
