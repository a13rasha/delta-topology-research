from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class StateNode:
    label: str
    payload: str
    parent: str | None = None


class StateTopology:
    def __init__(self):
        self.states: dict[str, StateNode] = {}

    def add_state(self, label: str, payload: str, parent: str | None = None):
        self.states[label] = StateNode(label=label, payload=payload, parent=parent)

    def transition(self, source: str, target: str) -> Tuple[str, str]:
        if source not in self.states or target not in self.states:
            raise KeyError("source or target state is undefined")
        return self.states[source].payload, self.states[target].payload


def build_demo_graph() -> StateTopology:
    graph = StateTopology()
    graph.add_state("A", "666666")
    graph.add_state("B", "936693", parent="A")
    return graph
