from typing import TypedDict, List
from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph, START, END
from transformers import AutoModel, AutoTokenizer


class AgentState(TypedDict):
    messages: List[HumanMessage]


tokenizer = AutoTokenizer.from_pretrained("D:\\models\\chatglm3-6b", trust_remote_code=True)
llm = AutoModel.from_pretrained("D:\\models\\chatglm3-6b", trust_remote_code=True).half().cuda()


def process(state: AgentState, ) -> AgentState:
    response = llm.chat(tokenizer, state["messages"][0].content, history=[])
    print(f"\nAI: {response[0]}")
    return state


graph = StateGraph(AgentState)
graph.add_node("process", process)
graph.add_edge(START, "process")
graph.add_edge("process", END)
agent = graph.compile()

user_input = input("Enter: ")
while user_input != "exit":
    aa = {"messages": [HumanMessage(content=user_input)]}
    agent.invoke({"messages": [HumanMessage(content=user_input)]})
    user_input = input("Enter: ")
