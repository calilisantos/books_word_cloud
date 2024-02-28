SOURCE_PATH: str = "src/data/raw_content"
TARGET_PATH: str = "src/data/raw_content.parquet"
TITLE_PATTERN: str = r"Title:\s*(.*?)\n"
AUTHOR_PATTERN: str = r"Author:\s*(.*?)\n"
READ_MODE: str = "r"
RAW_CONTENT_COLUMNS: list = ['title', 'author', 'content']
WRITE_MODE: str = "overwrite"
