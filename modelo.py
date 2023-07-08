import gurobipy as gp

class Modelo:
    def __init__(self, decision_variables, objective_function, constraints):
        self.model = gp.Model("Modelo")

        for variable in decision_variables:
            self.model.addVar(name=variable)
        
        for constraint in constraints:
            self.model.addConstr(constraint) # Validar como converter
        
        self.model.setObjective(objective_function) # Validar como converter

    def solve_model(self):
        self.model.optimize()
        if self.model.status == gp.GRB.OPTIMAL:
            for var in self.model.getVars():
                print(f"{var.varName}: {var.x}")