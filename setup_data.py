#!/usr/bin/env python3
"""
Convert the scraped CSV to Parquet partitions
"""
import polars as pl
from datetime import datetime
import os

def convert_csv_to_parquet():
    """Convert swiggy_scraped.csv to partitioned Parquet format"""
    
    print("Reading CSV file...")
    df = pl.read_csv("swiggy_scraped.csv")
    
    print(f"Loaded {len(df)} rows")
    print(f"Columns: {df.columns}")
    
    # Parse datetime columns with IST timezone
    df = df.with_columns([
        pl.col("at").str.strptime(pl.Datetime, format="%Y-%m-%d %H:%M:%S").dt.replace_time_zone("Asia/Kolkata"),
        pl.when(pl.col("repliedAt") != "").then(
            pl.col("repliedAt").str.strptime(pl.Datetime, format="%Y-%m-%d %H:%M:%S").dt.replace_time_zone("Asia/Kolkata")
        ).otherwise(None).alias("repliedAt"),
        pl.col("reviewId").alias("review_id"),
        pl.col("userName").alias("user_name"),
        pl.col("content").alias("content_raw"),
        pl.col("content").str.strip_chars().str.to_lowercase().alias("content_clean"),
        pl.col("score").cast(pl.Int8),
        pl.col("thumbsUpCount").cast(pl.Int32).alias("thumbs_up"),
        pl.col("reviewCreatedVersion").alias("app_version"),
        pl.col("replyContent").alias("reply_text"),
        pl.col("content").str.split(" ").list.len().alias("length_tokens"),
    ])
    
    # Add computed columns
    df = df.with_columns([
        (pl.col("length_tokens") < 10).alias("is_short"),
        pl.when(pl.col("app_version") == "").then(None).otherwise(pl.col("app_version")).alias("app_version"),
    ])
    
    # Rename for better schema
    df = df.select([
        "review_id",
        "user_name",
        "content_raw",
        "content_clean",
        "score",
        "thumbs_up",
        "at",
        "reply_text",
        "repliedAt",
        "app_version",
        "length_tokens",
        "is_short",
    ])
    
    # Extract date for partitioning
    df = df.with_columns([
        pl.col("at").dt.date().alias("dt")
    ])
    
    # Write to partitioned Parquet
    for date in df["dt"].unique().sort():
        date_str = date.strftime("%Y-%m-%d")
        partition_path = f"data/clean/app=swiggy/dt={date_str}"
        os.makedirs(partition_path, exist_ok=True)
        
        df_partition = df.filter(pl.col("dt") == date)
        
        # Remove dt column before saving
        df_partition = df_partition.drop("dt")
        
        output_file = f"{partition_path}/reviews.parquet"
        df_partition.write_parquet(output_file)
        print(f"Wrote {len(df_partition)} rows to {output_file}")
    
    print("\nConversion complete!")
    print(f"\nSummary:")
    print(f"Total rows: {len(df)}")
    print(f"Date range: {df['at'].min()} to {df['at'].max()}")
    print(f"Unique dates: {df['dt'].unique().len()}")

if __name__ == "__main__":
    convert_csv_to_parquet()

