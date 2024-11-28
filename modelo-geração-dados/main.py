import pandas as pd
from ctgan import CTGAN

# Carregar o CSV original
patients_data = pd.read_csv("/content/The_Cancer_data_1500_V2.csv")

# Treinar o modelo CTGAN
model = CTGAN(epochs=10)
model.fit(patients_data)

# Criar dados sintéticos
synthetic_data = model.sample(150000)

# Salvar os novos dados em um arquivo CSV
synthetic_data.to_csv("/content/The_Cancer_data_Generated.csv", index=False)

print("Dados sintéticos gerados e salvos em 'The_Cancer_data_Generated.csv'.")