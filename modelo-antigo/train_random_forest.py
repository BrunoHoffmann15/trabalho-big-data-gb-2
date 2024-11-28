import time
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, recall_score, f1_score, precision_score

print("Iniciando Preparação dos dados.")
start_time_prep_data = time.time()

# Obtém os dados do arquivo
patients_data = pd.read_csv("./resources/The_Cancer_data_Generated.csv")

# Divisão dos dados em X (features) e Y (classe)
X = patients_data.iloc[:, 0:8].values
y = patients_data.iloc[:, 8].values

# Criação do OneHotEncoder para coluna 4 (Genetic Risk)
one_hot_encoder = ColumnTransformer(transformers=[('OneHot', 
                                                   OneHotEncoder(), 
                                                   [4])], 
                                                   remainder='passthrough')
X = one_hot_encoder.fit_transform(X)

# Transformando os dados para a mesma escala
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Divisão dos dados em treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, 
                                                    random_state=42)

end_time_prep_data  = time.time()
print(f"Preparação dos dados finalizada, tempo de espera: {end_time_prep_data - start_time_prep_data} segundos.")


# Criação e treinamento do modelo Random Forest
print("Começando treinamento.")

start_time_train_data = time.time()
classifier = RandomForestClassifier(n_estimators=300)
classifier.fit(X_train, y_train)
end_time_train_data = time.time()

print(f"Treinamento finalizado, tempo de espera: {end_time_train_data - start_time_train_data} segundos.")

# Verificação de Métricas.
print("Executando modelo sobre os dados de testes")
start_time_test_data = time.time()
y_pred = classifier.predict(X_test)
end_time_test_data = time.time()
print(f"Modelo sobre os dados de testes executado, tempo de espera: {end_time_test_data - start_time_test_data} segundos.")

print("Verificando métricas!")
start_time_metrics_data = time.time()
accuracy = accuracy_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
end_time_metrics_data = time.time()

print(f"Métricas verificadas, tempo de espera: {end_time_metrics_data - start_time_metrics_data} segundos.")
print(f"Acurácia: {accuracy * 100}%")
print(f"Precisão: {precision * 100}%")
print(f"F1-Score: {f1 * 100}%")
print(f"Recall: {recall * 100}%")