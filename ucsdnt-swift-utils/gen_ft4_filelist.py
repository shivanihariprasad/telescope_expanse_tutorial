#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
from os import environ
import argparse
from swiftclient.service import SwiftService, SwiftError

def list_files(container):
    items = []
    
    with SwiftService(options=options) as swift:
        list_parts_gen = swift.list(container=container)
        for page in list_parts_gen:
            if page["success"]:
                for item in page["listing"]:

                    i_name = item["name"]
                    i_size = int(item["bytes"])
                    i_etag = item["hash"]
                    items.append(
                        (i_name, i_size, i_etag)
                    )
            else:
                raise page["error"]
    return items

def filetup_to_df(file_tups):
    df = pd.DataFrame(file_tups, columns=['filename', 'byte_size', 'hash'])
    df['ts_seconds'] = df.filename.apply(lambda x: int(x.split('.')[1]))
    df['datetime'] = pd.to_datetime(df.ts_seconds, unit='s')
    return df

if __name__ == "__main__":
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--CONTAINER", type=str, required=True, help="")
    parser.add_argument("--OUT_FILE", type=str, required=True, help="")
    args = parser.parse_args()

    OUT_FILE  = args.OUT_FILE
    CONTAINER = args.CONTAINER

    # Set swift credentials
    options = {
        "auth_version": environ.get('OS_IDENTITY_API_VERSION'),  # Should be '3'
        "os_username": environ.get('OS_USERNAME'),
        "os_password": environ.get('OS_PASSWORD'),
        "os_project_name": environ.get('OS_PROJECT_NAME'),
        "os_project_domain_name": environ.get('OS_PROJECT_DOMAIN_NAME'),
        "os_auth_url": environ.get('OS_AUTH_URL'), 
    }

    # Call swift, save results
    ft4_2023_files = list_files(CONTAINER)
    ft4_2023_df = filetup_to_df(ft4_2023_files)
    ft4_2023_df.to_parquet(OUT_FILE, compression='gzip')
