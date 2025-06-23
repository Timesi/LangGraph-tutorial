from typing import TypedDict
from langgraph.graph import StateGraph


class AgentState(TypedDict):
    name: str
    age: str
    final: str


def first_node(state: AgentState) -> AgentState:
    state["final"] = f'Hi {state["name"]}!'
    return state


def second_node(state: AgentState) -> AgentState:
    state["final"] = state["final"] + f'You are {state["age"]} years old!'
    return state

# 这个对象代表一个任务流程图，用于管理任务节点和流程逻辑
graph = StateGraph(AgentState)

# 添加节点
graph.add_node("first_node", first_node)
graph.add_node("second_node", second_node)

# 设置流程图的入口节点为"first_node"
graph.set_entry_point("first_node")
# 在流程图中添加一条从"first_node"节点到"second_node"节点的边
graph.add_edge("first_node", "second_node")
# 设置流程图的出口节点为"second_node"
graph.set_finish_point("second_node")
app = graph.compile()

result = app.invoke({"name": "John", "age": "30"})
print(result)