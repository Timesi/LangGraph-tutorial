from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class AgentState(TypedDict):
    number1: int
    operation: str
    number2: int
    finalNumber: int


def adder(state: AgentState) -> AgentState:
    state["finalNumber"] = state["number1"] + state["number2"]
    return state


def subtractor(state: AgentState) -> AgentState:
    state["finalNumber"] = state["number1"] - state["number2"]
    return state


def decide_next_node(state: AgentState) -> AgentState:
    if state["operation"] == "+":
        return "addition_operation"
    elif state["operation"] == "-":
        return "subtraction_operation"


graph = StateGraph(AgentState)

graph.add_node("add_node", adder)
graph.add_node("subtract_node", subtractor)
graph.add_node("router", lambda state:state) # passthrough function

graph.add_edge(START, "router")

# 在"router"节点添加条件分支边：
# 根据路由函数decide_next_node的返回值决定下一步执行哪个节点：
# 如果返回"addition_operation"，则进入"add_node"执行加法；
# 如果返回"subtraction_operation"，则进入"subtract_node"执行减法
graph.add_conditional_edges(
    "router",
    decide_next_node,
    {
        # Edge: Node
        "addition_operation": "add_node",
        "subtraction_operation": "subtract_node"
    }

)

graph.add_edge("add_node", END)
graph.add_edge("subtract_node", END)

app = graph.compile()

initial_state_1 = AgentState(number1 = 10, operation="-", number2 = 5)
print(app.invoke(initial_state_1))
# 调用app的invoke方法，传入初始状态initial_state_1，执行整个流程：
# 流程从START开始 → 进入router节点 → 根据operation="-"路由到subtract_node执行减法 → 最后到END结束
# 输出最终状态，其中finalNumber应为10-5=5，预期输出：{'number1': 10, 'operation': '-', 'number2': 5, 'finalNumber': 5}