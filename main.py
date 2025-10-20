from datetime import datetime
from lightstreamer_reader.interfaces import DATA_SCHEMA

import polars as pl
import os


def read(fn: str):
    if os.path.exists(fn):
        return pl.read_parquet(fn)
    return pl.DataFrame(schema=DATA_SCHEMA.schema)


def write(df: pl.DataFrame, fn: str):
    _df = read(fn)
    stacked = _df.vstack(df)
    stacked.write_parquet(fn)
    return stacked


if __name__ == "__main__":
    from lightstreamer_reader.pissstream import fetch_current_capacity

    import argparse
    from time import sleep

    parser = argparse.ArgumentParser(
        description="Fetch and write ISS urine tank capacity to a parquet file with timestamps"
    )
    parser.add_argument("-pf", "--parquet_filepath", default="./data/log.parquet")
    args = parser.parse_args()
    while True:
        df = write(
            pl.DataFrame(
                {
                    DATA_SCHEMA.dt: datetime.now(),
                    DATA_SCHEMA.val: fetch_current_capacity(),
                }
            ),
            args.parquet_filepath,
        )
        sleep(5)
