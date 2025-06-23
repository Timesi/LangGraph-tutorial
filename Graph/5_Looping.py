from langgraph.graph import StateGraph, END
import random
from typing import Dict, List, TypedDict


class AgentState(TypedDict):
    name: str
    number: List[int]
    counter: int


def greeting_node(state: AgentState) -> AgentState:
    state["name"] = f'Hi there, {state["name"]}'
    state["counter"] = 0
    return state


def random_node(state: AgentState) -> AgentState:
    state["number"].append(random.randint(1, 10))
    state["counter"] += 1
    return state


def should_continue(state: AgentState) -> AgentState:
    if state["counter"] < 5:
        print("ENTERING LOOP", state["counter"])
        return "loop"
    else:
        return "exit"


graph = StateGraph(AgentState)

graph.add_node("greeting", greeting_node)
graph.add_node("random", random_node)
graph.add_edge("greeting", "random")

graph.add_conditional_edges(
    "random",
    should_continue,
    {
        # 如果 should_continue 返回 "loop"，则继续执行 "random" 节点
        "loop": "random",
        # 如果 should_continue 返回 "exit"，则结束流程
        "exit": END,
    }
)

graph.set_entry_point("greeting")

app = graph.compile()

print(app.invoke({"name":"Vaibhav", "number":[], "counter":-100}))
