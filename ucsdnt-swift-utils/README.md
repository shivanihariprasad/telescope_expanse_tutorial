# Usage Instructions
---

## 1. Environment Setup

`requirements.txt` lists dependencies needed to run this code.

Notably, Swift's python libraries include `python-swiftclient` and `python-keystoneclient`.

## 2. Generating FT4 Dataframes

```bash
# Replace with location of the Swift credentials file given to you
source ~/.limbo_creds 

# Used to generate the sample parquet file in this repository
python3 gen_ft4_filelist.py --CONTAINER="telescope-ucsdnt-avro-flowtuple-v4-2023" --OUT_FILE="ft4_2023_files.parquet.gzip"
```

## 3. Plotting daily file counts

Start a `jupyter-lab` server instance and run `plot_ft4_filelist.ipynb`.