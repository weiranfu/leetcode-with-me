---
title: Object Oriented Design Summary
tags:
  - common
  - tricky
categories:
  - Summary
date: 2020-10-09 23:11:34
---

## 如何准备OO Design

转自：@yaobinwen https://github.com/yaobinwen/job_hunting

参考 Cracking the Coding Interview

我认为Object-oriented design这方面的问题，面试官更多考察的是你是否有系统化的方法去分析问题并逐步细化地建立起object-oriented的模型。OO Design的题似乎在面试中并不多见。

<!--more-->

OO Design的题目一般需要UML相关的知识做准备：

- class diagram (类图): 最常用
- sequence diagram (时序图): 最常用
- state machine diagram (状态机图): 在分析系统中某实体的状态时可能会用到。

我看过Cracking the Coding Interview (6th edition)中关于OO Design的章节。这本书里面介绍的分析和设计流程有4个步骤：

- 澄清题目中含糊不清的地方。Handle Ambiguity. You should inquire *who* is going to use and *how* they are goint to use. *who, what, where, when, how, why*

- 定义出核心的对象。Define the Core Objects. 

- 分析对象之间的关系，例如包含与被包含关系，数量上的关系，继承上的关系，等等。

  Which objects are members of which other objects? Do any objects inherit from any other objects? Are relationships many-to-many or one-to-one?

- 分析对象可以具有的行为(也就是各个class的methods)。Investigate Actions. 

这种分析流程是以对象为核心展开的，所以在第二步的时候就要定义问题中涉及到的对象。但我认为这样的流程在实际分析当中可能遇到的最大的问题，就是定义出的对象以及对象具有的行为可能无法完整地支持所有的业务流程。假如用ATM设计来作为例子的话，当我们只需要处理“取款”这一项业务的时候，可能我们使用以对象为核心的分析方法是可以做出完整的分析的。但是一旦业务流程增多(实际工作中的问题领域所涉及到的业务流程往往会非常多)，每个流程又涉及到大量的对象，往往会遗漏掉需要对象。另一个问题是设计的对象的methods未必能完整地覆盖到所有的业务流程的需要。

因此我在做OO Design的时候，一般是以业务流程的分析为核心而展开的。这个分析过程是：

- 列举出需要设计的所有的业务流程。
- 选取一项业务流程，详细描述其内部细节的步骤。每个步骤都要用完整的主谓宾结构的句子描述。
- 将每个步骤中的主语、谓语和宾语重点标识出来。主语和宾语是将来可能建立的class，而谓语就是可能的methods。
- 构建初始的OO模型，包括所有的class，以及class之间的关联关系和数量关系。以及所有业务流程的sequence图，以及sequence图上各个method的参数和返回值。
- 改进OO模型，例如对具有共同特征的class进行抽象，抽取出公共的abstract class。
- 重复2~5步分析下一项业务流程，并且把分析出来的新内容添加到已有的OO模型中，并不断调整模型使之适应新的业务流程。直到所有的业务流程都分析完毕。

如果是学过软件工程的话，我的方法其实很简单：

- 编写详细的系统use cases。
- 识别use cases中出现的名词和动词，它们可能是OO模型中的class和methods。

还是举ATM的例子。这里我们只考虑一台ATM机的情形，于是不需要处理分布式系统中的scalability、availability和data consistency的问题。(我面试中碰到的实际问题是设计Starcraft游戏。但这个例子对很多不怎么玩游戏的同学就不适用了。)

如果我在面试中碰到这个ATM软件系统的设计题，我会这样来做：

- 列举出需要设计的业务流程：取款；存款。其实还有别的业务，比如单纯的查询余额什么的，不过这里限于篇幅，我就不列举所有的功能了。
- 对于“取款”这项业务，列出详细的执行步骤：
  - 用户插入银行卡到ATM。
  - ATM提示取回银行卡，并吐出银行卡。
  - ATM提示输入密码。
  - 用户输入密码。
  - ATM验证密码。如果通过，则继续下一步；否则提示密码错误，并跳回第3步。
  - ATM显示功能菜单。
  - 用户点击“取款”按钮。
  - ATM提示输入取款金额。
  - 用户输入取款金额。
  - ATM吐出指定数额的现钞。
- 标记出每个步骤中的主谓宾。在上面的步骤中，主语和宾语用下划线标识；谓语用加黑的斜体标识。
- 建立初始的OO模型。在上面的业务流程分析中，我们一共总结出如下名词：用户，银行卡，ATM，密码，功能菜单，“取款”按钮，取款金额，现钞。同时也总结出如下的动词：插入，吐出，提示，输入，验证，显示，点击。每个名词可能是OO模型中的class，每个动词可能是某个class的method。再分析不同对象之间的关联关系，于是我们可以得到一个初步的(但也是粗糙的)OO模型：

![初始模型](https://cdn.jsdelivr.net/gh/weiranfu/image-hosting@main/img/leetcode/OO_Design_01.png)

- 改进OO模型。一开始的OO模型很可能非常不完善，甚至有些部分可能还不正确。我们可以在后面不断的分析当中逐步修正。例如，“用户”很可能是属于我们所关心的系统的边界外边的，因此不应该放到系统内。“密码”或许是不需要单独建立class去描述，因为一般情况下银行的密码都是一串数字，所以很可能用一个普通的整数类型就可以表达。“取款金额”可以用Java内置的Currency类型来表示，所以也不必要单独建立class。“提示”和“显示”这两个行为其实都是在ATM的屏幕上展现信息，所以可以合并成一个行为，但此时被显示的内容就需要进行一定的抽象，例如让它们都实现一个IDisplayable接口。这样改善过的OO模型可能变成这样：

![改进模型](https://cdn.jsdelivr.net/gh/weiranfu/image-hosting@main/img/leetcode/OO_Design_02.png)

- 但这个OO模型仍然不完善。例如，“取款按钮”应该是被显示在功能菜单上，所以属于“功能菜单”看上去更合适。“点击”的操作也是实施在“功能菜单”上，所以属于“功能菜单”看上去更合适。“输入”的操作是在具体的提示消息界面中完成的，例如输入密码或取款金额，因此“输入”的操作放到“提示消息”中似乎更合适。而这样继续分析下去后，可能又可以尝试进一步把这些输入的和点击的操作抽象成某种接口。不过这些改进都可以逐步来完成。
- 考虑下一个业务流程，重复2~7步。不断地把新的业务流程加入到已有的模型中，同时不断地调整模型使之能cover目前已分析的所有流程。直到把所有业务流程都分析完毕。

总之，OO Design往往没有唯一正确的答案，但需要有一个比较系统的分析方法，让面试官相信你的分析是全面的，而不是那种毫无章法随便乱撞的方式来分析。



