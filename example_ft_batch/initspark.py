import os
import socket

from pyspark.sql import SparkSession

# Extracted from https://github.com/CAIDA/expanse_spark/blob/main/SparkPOC.ipynb

def connect():
    user = "bjd"
    hostname = socket.getfqdn()

    os.environ["HADOOP_OPTS"] = (
        "-Djava.library.path=/cm/shared/apps/spack/cpu/opt/spack/linux-centos8-zen/gcc-8.3.1/hadoop/3.2.2/lib/native"
    )
    os.environ["PYSPARK_SUBMIT_ARGS"] = (
        r"--jars /expanse/lustre/scratch/bjd/temp_project/spark-3.2.1/ext_jars/* --packages org.apache.spark:spark-avro_2.12:3.2.1 pyspark-shell"
    )
    os.environ["SPARK_LIB"] = os.environ["SPARK_HOME"]

    UCSD_NT_S3_ACCESS_KEY = ""
    UCSD_NT_S3_SECRET_KEY = ""
    MASTER_URL = rf"spark://{hostname}:7077"

    return (
        SparkSession.builder.master(MASTER_URL)
        .appName("spark-cluster")
        .config(
            "fs.s3a.aws.credentials.provider",
            "org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider",
        )
        .config("fs.s3a.access.key", UCSD_NT_S3_ACCESS_KEY)
        .config("fs.s3a.secret.key", UCSD_NT_S3_SECRET_KEY)
        .config("fs.s3a.endpoint", "https://hermes.caida.org")
        .config("fs.s3a.path.style.access", "true")
        .config("fs.s3a.block.size", "64M")
        .config("fs.s3a.readahead.range", "128K")
        .config("fs.s3a.experimental.input.fadvise", "sequential")
        .config("fs.s3a.connection.maximum", 256)
        .config("spark.driver.cores", "2")
        .config("spark.driver.memory", "2G")
        # the values below this line are candidate for deletion, test it please
        .config("io.file.buffer.size", "67108864")
        .config("spark.submit.deploymode", "client")
        .config("spark.buffer.size", "67108864")
        .config("spark.network.timeout", "300s")
        .config(
            "spark.sql.files.ignoreCorruptFiles",
            "true",  # Set this when analyzing periods of high volatility, during which there may be corrupt files
        )
        .config("spark.sql.session.timeZone", "UTC")
        .getOrCreate()
    )
