from langgraph.graph import START, StateGraph,END
from typing_extensions import TypedDict

class State(TypedDict):
    text: str

def node_a(state: State) -> dict:
    return {"text": state["text"] + "a"}

def node_b(state: State) -> dict:
    return {"text": state["text"] + "b"}

def should_continue(state:State)->str:
    return "true" if state["text"] == "abab" else "false"



graph = StateGraph(State)
graph.add_node("node_a", node_a)
graph.add_node("node_b", node_b)

graph.add_edge(START, "node_a")
graph.add_edge("node_a", "node_b")
graph.add_conditional_edges("node_b", should_continue, {"true": END, "false": "node_a"})

compiled_graph = graph.compile()
print(compiled_graph.invoke({"text": ""}))

print(compiled_graph.get_graph().draw_mermaid())


# {'text': 'ab'}