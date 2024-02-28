from src.configs import transform as confs
from pyspark.ml.feature import StopWordsRemover, Tokenizer
from pyspark.sql import DataFrame, functions as F
from wordcloud import WordCloud


class BooksService:
    def __init__(self, dataframe: DataFrame):
        self._data = dataframe
        self._words_count = DataFrame
        self._top_words = list
        self._dict_data = dict
        self._word_cloud = WordCloud

    def _clean_text(self):
        self._data = (
            self._data
            .withColumn(
                confs.TEXT_COLUMN,
                F.regexp_replace(
                    F.col(confs.TEXT_COLUMN),
                    confs.NON_WORDS_PATTERN,
                    ''
                )
            )
        )

    def _tokenize_text(self):
        tokenizer = Tokenizer(
            inputCol=confs.TEXT_COLUMN,
            outputCol=confs.WORD_COLUMN
        )

        self._data = (
            tokenizer.transform(self._data)
            .drop(confs.TEXT_COLUMN)
        )

    def _remove_stop_words(self):
        remover = StopWordsRemover(
            inputCol=confs.WORD_COLUMN,
            outputCol=confs.FILTERED_COLUMN
        )
        self._data = (
            remover.transform(self._data)
            .drop(confs.WORD_COLUMN)
        )

    def _count_words(self):
        self._words_count = (
            self._data
            .withColumn(
                confs.FILTERED_COLUMN,
                F.explode(
                    confs.FILTERED_COLUMN
                )
            )
                .groupBy(confs.FILTERED_COLUMN)
                    .count()
                        .orderBy(
                            'count',
                            ascending=False
                        )
        )

    def _remove_noise_words(self):
        self._words_count = (
            self._words_count
            .filter(
                F.length(confs.FILTERED_COLUMN) > confs.NOISE_WORDS_LENGTH
            )
        )

    def _get_top_words(self):
        self._top_words = (
            self._words_count
            .limit(confs.COMMON_WORDS_SAMPLE)
        )

    def _set_dict_data(self):
        self._dict_data = {row[confs.FILTERED_COLUMN].title(): row['count'] for row in self._top_words.collect()}

    def _set_word_cloud(self):
        self._word_cloud = (
            WordCloud(
                width=confs.WORDCLOUD_WIDTH,
                height=confs.WORDCLOUD_HEIGHT,
                background_color=confs.WORDCLOUD_BACKGROUND_COLOR
            ).generate_from_frequencies(self._dict_data)
        )

    def _save_word_cloud(self):
        self._word_cloud.to_file(confs.WORDCLOUD_IMAGE_NAME)

    def create_word_cloud(self):
        self._clean_text()
        self._tokenize_text()
        self._remove_stop_words()
        self._count_words()
        self._remove_noise_words()
        self._get_top_words()
        self._set_dict_data()
        self._set_word_cloud()
        self._save_word_cloud()
        return self
