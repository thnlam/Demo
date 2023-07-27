def get_current_date(spark):
    opDF = spark.sql(""" Select current_date """)
    print("Validate the spark object by printing Current date - " + str(opDF.collect()))