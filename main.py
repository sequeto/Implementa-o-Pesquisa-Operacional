# João Pedro Sequeto - 201776022
# Felipe - -

import modelo
import file

txt_file = file.File('dados.csv', 'csv')

# Leitura de Dados
data = txt_file.read_file()

print(data)
# Criação do Modelo
# Execução do Solver
# Exportação de Resultados