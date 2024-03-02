from pyspark.sql import SparkSession

raw_content = [
    {
        "content": "When he was nearly thirteen, my brother Jem got his arm badly broken at the elbow. When it healed, and Jem's fears of never being able to"
    }
]

raw_content_df = SparkSession.builder.getOrCreate().createDataFrame(raw_content)
