from statemachine import StateMachine, State

class TwoStateDiagram(StateMachine):
    # State diagram with 2 states
    states = [State('State1', initial=True), State('State2')]

    def __init__(self):
        for from_state in self.states:
            for to_state in self.states:
                transition_name = f"transition_from_{from_state.name}_to_{to_state.name}"
                setattr(self, transition_name, from_state.to(to_state))

class ThreeStateDiagram(StateMachine):
    # State diagram with 3 states
    states = [State('State1', initial=True), State('State2'), State('State3')]
    transition_matrix = [
        ('b', 'a', 'd'),
        ('b', None, 'b'),
        ('c', 'a', 'd')
    ]

    def __init__(self):
        for i, from_state in enumerate(self.states):
            for j, to_state in enumerate(self.states):
                transition_label = self.transition_matrix[i][j]
                if transition_label is not None:
                    transition_name = f"transition_{i+1}_to_{j+1}_{transition_label}"
                    setattr(self, transition_name, from_state.to(to_state, label=transition_label))

# Instantiate the state machine
diagram = ThreeStateDiagram()
print(diagram.current_state)

