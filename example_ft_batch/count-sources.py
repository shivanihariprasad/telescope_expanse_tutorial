# %%
# Init

import initspark
import pyspark.sql.functions as f

spark = initspark.connect()
spark

# Read one day of data, count and save


def load_ft(year, month="*", day="*", hour="*"):
    if month != "*":
        month = f"{month:02}"
    if day != "*":
        day = f"{day:02}"
    if hour != "*":
        hour = f"{hour:02}"

    basepath = f"s3a://telescope-ucsdnt-avro-flowtuple-v4-{year}/datasource=ucsd-nt"
    fullpath = f"{basepath}/year={year}/month={month}/day={day}/hour={hour}"

    return spark.read.format("avro").option("basePath", basepath).load(fullpath)


for d in range(1, 31):
    dfs = load_ft(2019, 5, d, "*")

    dfs_sources = dfs.groupby(["year", "month", "day", "hour"]).agg(
        f.count_distinct("src_ip").alias("src_ip_count")
    )

    dfs_sources.coalesce(1).write.option("header", "true").option("sep", ",").mode(
        "append"
    ).csv(
        "/expanse/lustre/projects/sds193/bjd/darknet-observability/output/count_sources/dfs_sources"
    )
