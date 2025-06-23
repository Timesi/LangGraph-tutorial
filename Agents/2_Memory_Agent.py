from typing import TypedDict, List, Union
from langchain_core.messages import HumanMessage, AIMessage
from langgraph.graph import StateGraph, START, END
from transformers import AutoModel, AutoTokenizer


class AgentState(TypedDict):
    messages: List[Union[HumanMessage, AIMessage]]


tokenizer = AutoTokenizer.from_pretrained("D:\\models\\chatglm3-6b", trust_remote_code=True)
llm = AutoModel.from_pretrained("D:\\models\\chatglm3-6b", trust_remote_code=True).half().cuda()


def process(state: AgentState) -> AgentState:
    response = llm.chat(tokenizer, state["messages"][0].content, history=[])

    state["messages"].append(AIMessage(content=response[0]))
    print(f"\nAI: {response[0]}")
    print("CURRENT STATE:", state["messages"])

    return state


graph = StateGraph(AgentState)
graph.add_node("process", process)
graph.add_edge(START, "process")
graph.add_edge("process", END)
agent = graph.compile()


conversation_history = []

user_input = input("Enter: ")
while user_input != "exit":
    conversation_history.append(HumanMessage(content=user_input))
    result = agent.invoke({"messages": conversation_history})
    conversation_history = result["messages"]
    user_input = input("Enter: ")


with open("logging.txt", "w") as file:
    file.write("Your Conversation Log: \n")

    for message in conversation_history:
        if isinstance(message, HumanMessage):
            file.write(f"You: {message.content}\n")
        elif isinstance(message, AIMessage):
            file.write(f"AI: {message.content}\n")
    file.write("End of Conversation")

print("Conversation saved to logging.txt")