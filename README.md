# LangGraph基础概念
## State
State是一个共享的数据结构，它保存整个应用程序的当前信息或上下文。简单来说，它就像应用程序的内存，跟踪节点在执行时可以访问和修改的变量和数据。

## Nodes
Nodes是在图中执行特定任务的单个函数或操作。每个节点接收输入（通常是当前状态），对其进行处理，并生成输出或更新状态。

## Graph
Graph是一个总体结构，它描绘了不同的任务（节点）是如何连接和执行的。可以直观地表示工作流，显示各种操作之间的顺序和条件路径。

## Edges
Edges时节点之间的连接关系，它决定了执行流程的走向。

## Conditional Edges
Conditional Edges是一种特殊的连接方式，会根据针对当前状态所应用的特定条件或逻辑来决定接下来要执行的节点。

## START
START节点时一个虚拟入口，标志着工作流的起始位置，该节点本身不会执行任何操作，而是作为图执行过程中的指定起始点。

## END
END节点表示工作流的结束，到达此节点后，图的执行过程即停止，这意味着所有操作均已完成。

## Tools
Tools节点时专门的功能或者程序，节点可以利用他们来执行特定的任务，例如从API中获取数据。他们通过提供额外的功能来增强节点的能力。节点是图结构的一部分，而工具则是节点内部所使用的功能。

## ToolNode
ToolNode时一种特殊的节点，其主要职责是运行某个工具，他将工具的输出结果重新连接回State模块中，以便其他节点能够利用这些信息。

## StateGraph
StateGraph时LAngGraph中的一种类，用于构建和编译图结构，他负责管理Nodes、Edges和整体状态，确保工作流以统一的方式运行，并且数据能够在各个组件之间正确流动。

## Runnable
Runnable是一种经过标准化处理的，可执行的组建，它能在应用程序工作流中执行特定的任务，充当了一个基本的构建单元，使我们能够构建出模块化的系统。

## Messages
- Human Message：表示用户的输入
- System Message：用于提供模型的指令或上下文
- Function Message：表示function call的结果
- AI Message：表示AI模型生成的回复
- Tool Message：类似Function MEssage，但是是针对具体的工具使用

# Demo
ReAct.py对应流程图

![](./Agents/ReAct_Agent_Graph.png)


Drafter.py对应流程图

![](./Agents/Drafter.png)

RAG_Agent.py对应流程图

![](./Agents/RAG_Agent.png)


