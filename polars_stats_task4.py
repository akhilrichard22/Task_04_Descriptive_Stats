# Databricks notebook source
import polars as pl

# Detect dataset type
file_path = "file:/Workspace/Users/akvincen@syr.edu/facebook_ads.csv"  # CHANGE THIS
if "ads" in file_path:
    dataset = "facebook_ads"
elif "fb_posts" in file_path:
    dataset = "fb_posts"
else:  # twitter_posts
    dataset = "twitter_posts"

# Load data
df = pl.read_csv(file_path.replace("file:", ""))

print(f"Analyzing {dataset} ({df.height} records)")

# Dataset-specific configuration
if dataset == "facebook_ads":
    value_cols = ["estimated_audience_size", "estimated_impressions", "estimated_spend"]
    group1 = "page_id"
    group2 = ["page_id", "ad_id"]
elif dataset == "fb_posts":
    value_cols = ["Total Interactions", "Likes", "Comments", "Post Views"]
    group1 = "Facebook_Id"
    group2 = ["Facebook_Id", "post_id"]
else:  # twitter_posts
    value_cols = ["retweetCount", "replyCount", "likeCount", "viewCount"]
    group1 = "source"
    group2 = ["source", "id"]

# Convert numeric columns
for col in value_cols:
    if col in df.columns:
        df = df.with_columns(pl.col(col).str.replace_all(",", "").cast(pl.Float64))

# Global statistics
print("\n=== Global Statistics ===")
print(df.select([pl.mean(col).alias(f"mean_{col}") for col in value_cols]))
print(df.select([pl.min(col).alias(f"min_{col}") for col in value_cols]))
print(df.select([pl.max(col).alias(f"max_{col}") for col in value_cols]))

# Grouped analysis
print("\n=== Grouped by Primary Key ===")
print(df.group_by(group1).agg(
    pl.mean(value_cols[0]).alias("mean"),
    pl.min(value_cols[0]).alias("min"),
    pl.max(value_cols[0]).alias("max"),
    pl.count().alias("count")
).head(5))

print("\n=== Grouped by Composite Key ===")
print(df.group_by(group2).agg(
    pl.mean(value_cols[0]).alias("mean"),
    pl.min(value_cols[0]).alias("min"),
    pl.max(value_cols[0]).alias("max"),
    pl.count().alias("count")
).head(5))