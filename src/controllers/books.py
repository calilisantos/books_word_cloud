import logging
from pyspark.sql import SparkSession
from src.configs import logs as log_conf
from src.models.books import BooksModel
from src.services.books import BooksService
from src.views.books import BooksView


class BooksController:
    def __init__(self):
        self._logger = logging.getLogger(__name__)
        self._spark = (
            SparkSession.builder
                .appName('word_count_w_spark')
                    .master('local[*]')
                        .getOrCreate()
        )
        self._configure_logger()

    def _configure_logger(self):
        logging.basicConfig(
            format=log_conf.LOG_FORMAT,
            datefmt=log_conf.LOG_DATE_FORMAT,
            style=log_conf.LOG_STYLE,
            level=logging.INFO
        )

    def run(self):
        self._logger.info('Building the app...')
        books_model = BooksModel(self._spark)
        has_raw_content = books_model.check_raw_content()
        self._logger.info('Checking if the raw content exists...')
        if not has_raw_content:
            self._logger.info('Raw content not found. Creating it...')
            books_model.create_raw_dataframe()
            self._logger.info('Raw content created.')
        else:
            self._logger.info('Raw content found.')
        self._logger.info('Getting the books title...')
        try:
            books_title = books_model.get_books_title()
            self._logger.info('Books title retrieved.')
        except Exception as error:
            raise error(
                self._logger.error(f'Error retrieving the books title: {error}')
            )
        self._logger.info('Starting the app...')
        app = BooksView(books_title)
        app.set_title()
        book_selected = app.set_selectbox()
        self._logger.info(f'Book selected: {book_selected}')
        self._logger.info('Reading the book...')
        try:
            book = books_model.get_book(book_selected)
            self._logger.info('Book read.')
        except Exception as error:
            raise error(
                self._logger.error(f'Error reading the book: {error}')
            )
        self._logger.info('Get book author.')
        try:
            author = books_model.get_book_author()
            self._logger.info('Book author retrieved.')
        except Exception as error:
            raise error(
                self._logger.error(f'Error retrieving the book author: {error}')
            )
        self._logger.info('Create word cloud.')
        try:
            BooksService(book).create_word_cloud()
            self._logger.info('Word cloud created.')
        except Exception as error:
            raise error(
                self._logger.error(f'Error creating the word cloud: {error}')
            )
        app.set_book_title(book_selected)
        app.set_author(author)
        app.set_image()
