import gurobipy as gp

class Modelo:
    def __init__(self, decision_variables, objective_function, constraints):
        self.model = gp.Model("Modelo")
        self.decision_variables = []
        self.constraints = []

        for variable in decision_variables:
            self.decision_variables.append(self.model.addVar())
        
        for constraint in constraints:
            self.constraints.append(self.model.addConstr(constraint)) # Validar como converter
        
        self.objective_function = self.model.setObjective(objective_function) # Validar como converter

    def solve_model(self):
        self.model.optimize()