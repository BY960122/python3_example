from pyspark import SparkConf, SparkContext

if __name__ == '__main__':
    conf = SparkConf().setAppName("test").setMaster("local[*]")
    sc = SparkContext(conf=conf)
    sc.setLogLevel("INFO")
    rdd = sc.parallelize([1, 2, 3, 4, 5])

    print(rdd.reduce(lambda a, b: a + b))
