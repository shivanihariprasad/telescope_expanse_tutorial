
import pytz
import initspark

import pandas as pd
import pyspark
from pyspark import SQLContext
import pyspark.sql.functions as psf
import pyspark.sql.types as pst


spark = initspark.connect()
#spark


def generate_avro_uris(avro_filename, start_dt, end_dt, s3_pre_uri='s3a://telescope-ucsdnt-avro-flowtuple-v4-2024'):
    avro_df = pd.read_parquet(avro_filename)
    avro_df['datetime'] = pd.to_datetime(avro_df['datetime'])
    avro_df = avro_df.set_index('datetime')
    
    ### Select .avro's within timeframe
    selected_avros = avro_df[(avro_df.index >= start_dt) & (avro_df.index <= end_dt)]
    print(f'Avro filecount: {len(selected_avros)}')
    
    ### Build URI's
    selected_avro_uris = selected_avros.filename.apply(lambda x: f'{s3_pre_uri}/{x}').values
    print(f'Avro uri count: {len(selected_avro_uris)}')
    
    return selected_avro_uris



def load_ft_pyspark(avro_files):
    df = sqlcontext.read.format('avro').load(avro_files)
    df = df.withColumn('time', psf.to_utc_timestamp((df.time).cast(dataType=pst.TimestampType()), 'UTC'))
    # df = df.withColumn('time', psf.from_unixtime(df.time))
    return df


PROJECT = "csd939"

OUT_DIR = '/expanse/lustre/projects/{PROJECT}/{user}/shared_data/case_study_2'
START_1 = '2024-01-01 00:00'
END_1 = '2024-01-01 00:30'

start_1 = pd.to_datetime(START_1)
end_1 = pd.to_datetime(END_1)

sqlcontext = SQLContext(spark)

avro_filename = '../ft4_file_lists/ft4_2024_files.parquet.gzip'
s3_pre_uri = 's3a://telescope-ucsdnt-avro-flowtuple-v4-2024/'

avro_uris = generate_avro_uris(avro_filename, start_1, end_1, s3_pre_uri)
spark_df = load_ft_pyspark(list(avro_uris))

result = spark_df.groupby('dst_net').agg(
    psf.sum('packet_cnt'), 
    psf.countDistinct('src_ip')
).csv(
        f"{OUT_DIR}/dstnet_pkt_sources"
)