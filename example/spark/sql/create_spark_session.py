from pyspark.sql import SparkSession


def update_spark_log_level(spark, log_level='info'):
    spark.sparkContext.setLogLevel(log_level)
    log4j = spark._jvm.org.apache.log4j
    logger = log4j.LogManager.getLogger(log_level)
    return logger;


if __name__ == '__main__':
    # 构建SparkSession执行环境入口对象
    spark = SparkSession.builder. \
        appName("test"). \
        master("local[*]"). \
        getOrCreate()
    log = update_spark_log_level(spark, "info")
    log.info("-----------")
    # 通过SparkSession对象 获取 SparkContext对象
    sc = spark.sparkContext
    sc.setLogLevel("INFO")
    # SparkSQL的HelloWorld
    df = spark.read.csv("../data/input/stu_score.txt", sep=',', header=False)
    df2 = df.toDF("id", "name", "score")
    df2.printSchema()
    df2.show()

    df2.createTempView("score")

    # SQL 风格
    spark.sql("""
        select * from score where name='语文' limit 5
    """).show()

    # DSL 风格
    df2.where("name='语文'").limit(5).show()
