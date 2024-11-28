import time

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, FloatType, IntegerType
from pyspark.ml.feature import VectorAssembler, StandardScaler, OneHotEncoder, StringIndexer
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

def train_data() -> None:
    print("Iniciando conexão Spark.")

    # Abre sessão spark
    spark = SparkSession.builder.appName('PySpark-Get-Started').getOrCreate()

    print("Conexão iniciada com sucesso.")

    print("Iniciando Preparação dos dados.")

    # Define o schema dos dados
    start_time_prep_data = time.time()
    schema = StructType([
        StructField('Age', IntegerType(), nullable=False),
        StructField('Gender', IntegerType(), nullable=False),
        StructField('BMI', FloatType(), nullable=False),
        StructField('Smoking', IntegerType(), nullable=False),
        StructField('GeneticRisk', IntegerType(), nullable=False),
        StructField('PhysicalActivity', FloatType(), nullable=False),
        StructField('AlcoholIntake', FloatType(), nullable=False),
        StructField('CancerHistory', IntegerType(), nullable=False),
        StructField('Diagnosis', IntegerType(), nullable=False),
    ])

    # Importa os dados csv
    patients_data = spark.read.csv('./data/The_Cancer_data_1500_V2.csv', header=True, schema=schema)

    # Define features e classe
    features_one_hot_encoder = 'GeneticRisk'
    features = ['Age', 'Gender', 'BMI', 'Smoking', 'PhysicalActivity', 'AlcoholIntake', 'CancerHistory', 'GeneticRisk_encoded']

    # Realiza OneHotEncoder
    one_hot_encoder = OneHotEncoder(inputCol=features_one_hot_encoder, outputCol="GeneticRisk_encoded")
    encoded_data = one_hot_encoder.fit(patients_data).transform(patients_data)

    # Vetoriza as features
    assembler = VectorAssembler(inputCols=features, outputCol="features") 
    assembled_df = assembler.transform(encoded_data)

    # Escalonamento dos dados
    standardScaler = StandardScaler(inputCol="features", outputCol="features_scaled")
    scaled_df = standardScaler.fit(assembled_df).transform(assembled_df)

    # Dividindo o dataset entre treino e teste.
    splits = scaled_df.randomSplit([0.7, 0.3], seed=42)
    train_patients_data = splits[0]
    test_patients_data = splits[1]

    end_time_prep_data  = time.time()
    print(f"Preparação dos dados finalizada, tempo de espera: {end_time_prep_data - start_time_prep_data} segundos.")

    # Treinamento do modelo random forest
    print("Começando treinamento.")

    start_time_train_data = time.time()
    rf_classifier = RandomForestClassifier(featuresCol="features_scaled", labelCol="Diagnosis", numTrees=100)
    model = rf_classifier.fit(train_patients_data)
    end_time_train_data = time.time()
    
    print(f"Treinamento finalizado, tempo de espera: {end_time_train_data - start_time_train_data} segundos.")

    # Salvando o modelo
    model.write().overwrite().save("./data/trained_random_forest_spark")

    # Avaliação do modelo
    print("Executando modelo sobre os dados de testes")
    start_time_test_data = time.time()
    predictions = model.transform(test_patients_data)
    classifications = predictions.select("prediction", "Diagnosis")
    end_time_test_data = time.time()
    print(f"Modelo sobre os dados de testes executado, tempo de espera: {end_time_test_data - start_time_test_data} segundos.")

    # Verificando métricas
    print("Verificando métricas!")
    evaluator = MulticlassClassificationEvaluator(labelCol="Diagnosis", predictionCol="prediction")

    start_time_metrics_data = time.time()
    accuracy = evaluator.evaluate(classifications, {evaluator.metricName: "accuracy"})
    precision = evaluator.evaluate(classifications, {evaluator.metricName: "weightedPrecision"})
    recall = evaluator.evaluate(classifications, {evaluator.metricName: "weightedRecall"})
    f1_score = evaluator.evaluate(classifications, {evaluator.metricName: "f1"})
    end_time_metrics_data = time.time()

    print(f"Métricas verificadas, tempo de espera: {end_time_metrics_data - start_time_metrics_data}")
    print(f"Accuracy: {accuracy}")
    print(f"Precision: {precision}")
    print(f"Recall: {recall}")
    print(f"F1 Score: {f1_score}")


if __name__ == "__main__":
    train_data()