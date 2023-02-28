budget_january = input("¿Cuál es su presupuesto para enero?")
budget_february = input("¿Cuál es su presupuesto para febrero?")
budget_march = input("¿Cuál es su prupuesto para marzo?")

budget_january = int(budget_january)
budget_february = int(budget_february)
budget_march = int(budget_march)

budget_total = budget_january + budget_february + budget_march
print("La suma de los presupuestos es: ", budget_total)

budget_total = int(budget_total)

avg_budget = budget_total / 3
print("El presupuesto es: ", avg_budget)