from src.configs import data as data_config
from pathlib import Path
from pyspark.sql import DataFrame, SparkSession
from src.utils.text_search import get_match_text


class BooksModel:
    def __init__(self, spark: SparkSession) -> None:
        self._files_list = list()
        self._data_list = list()
        self._spark = spark
        self._data = DataFrame
        self._selected_book = DataFrame

    def check_raw_content(self) -> bool:
        return Path(data_config.TARGET_PATH).exists()

    def _set_files_list(self) -> None:
        self._files_list = [file.name for file in Path(data_config.SOURCE_PATH).iterdir() if file.is_file()]

    def _set_data_list(self) -> None:
        for file_name in self._files_list:
            with open(f"{data_config.SOURCE_PATH}/{file_name}", data_config.READ_MODE) as file:
                data = file.read()
                title = get_match_text(data, data_config.TITLE_PATTERN)
                author = get_match_text(data, data_config.AUTHOR_PATTERN)
                if not title:
                    print(f"Title not found in {file_name}")
                if not author:
                    print(f"Author not found in {file_name}")
                self._data_list.append((title, author, data))

    def create_raw_dataframe(self) -> None:
        self._set_files_list()
        self._set_data_list()
        self._spark.createDataFrame(
            self._data_list,
            data_config.RAW_CONTENT_COLUMNS
        ).write.mode(data_config.WRITE_MODE) \
            .parquet(data_config.TARGET_PATH)

    def _set_raw_dataframe(self) -> None:
        self._data = self._spark.read.parquet(data_config.TARGET_PATH)

    def get_books_title(self) -> list:
        self._set_raw_dataframe()
        titles = (
            self._data
                .select('title')
                    .distinct()
                        .orderBy('title')
                            .collect()
        )
        return [title['title'] for title in titles]

    def get_book(self, book_title: str) -> DataFrame:
        self._selected_book = (
            self._data
                .filter(self._data['title'] == book_title)
        )
        return self._selected_book

    def get_book_author(self) -> str:
        return (
            self._selected_book
                .select('author')
                    .distinct()
                        .collect()[0]['author']
        )
