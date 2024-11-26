# importa as libs do sparke as demais
from pyspark.sql import SparkSession
from pyspark.sql.functions import upper
from datetime import datetime, date
import pandas as pd
from pyspark.sql import Row

def train_data() -> None:
    spark = SparkSession.builder.appName('PySpark-Get-Started').getOrCreate()
    pandas_df = pd.DataFrame({
        'a': [1, 2, 3],
        'b': [2., 3., 4.],
        'c': ['string1', 'string2', 'string3'],
        'd': [date(2000, 1, 1), date(2000, 2, 1), date(2000, 3, 1)],
        'e': [datetime(2000, 1, 1, 12, 0), datetime(2000, 1, 2, 12, 0), datetime(2000, 1, 3, 12, 0)]
    })

    df = spark.createDataFrame(pandas_df)
    df.show()
    

if __name__ == "__main__":
    train_data()