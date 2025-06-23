from typing import Dict, TypedDict
from langgraph.graph import StateGraph      # 帮助设计和管理任务流程


# 创建一个AgentState，用于在程序运行过程中跟踪相关的信息
class AgentState(TypedDict):
    message: str


def greeting_node(state: AgentState) -> AgentState:
    """
    创建一个用于添加greeting message到state中的node
    :param state:
    :return:
    """
    state['message'] = "Hey " + state["message"] + ", how is your day going?"

    return state


# 创建一个StateGraph对象，指定状态类型为AgentState
# 这个对象代表一个任务流程图，用于管理任务节点和流程逻辑
graph = StateGraph(AgentState)

# 向流程图中添加一个名为“greeter”的节点
graph.add_node("greeter", greeting_node)

# 设置流程图的入口节点为“greeter”节点
graph.set_entry_point("greeter")
# 设置流程图的出口节点为“greeter”节点
graph.set_finish_point("greeter")

# 调用compile方法编译流程图，生成一个可执行的应用程序对象
app = graph.compile()

# 调用应用程序的invoke方法，传入初始状态{"message": "Alice"}
# 执行整个流程，从入口到出口，处理状态并返回最终结果
result = app.invoke({"message": "Alice"})
print(result["message"])

# # 在Jupyter Notebook中显示流程图
# from IPython.display import display, Image
# display(Image(app.get_graph().draw_mermaid_png()))
