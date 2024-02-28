from unittest import TestCase
from unittest.mock import patch, MagicMock
from src.controllers.books import BooksController
from pyspark.sql import SparkSession


class TestBooksController(TestCase):
    def setUp(self) -> None:
        mock_spark_session = MagicMock()
        SparkSession.builder = MagicMock()
        SparkSession.builder.getOrCreate.return_value = mock_spark_session
        self.controller = BooksController()

    def test_books_controller___logger_init(self):
        assert self.controller._logger is not None

    def test_books_controller__spark_init(self):
        assert self.controller._spark is not None

    @patch('src.controllers.books.BooksView')
    @patch('src.controllers.books.BooksService')
    @patch('src.controllers.books.BooksModel')
    def test_books_controller__model_raw_content_call(self, mock_books_model, mock_books_service, mock_books_view):
        mock_books_model_instance = mock_books_model.return_value
        self.controller.run()
        mock_books_model_instance.check_raw_content.assert_called_once()

    @patch('src.controllers.books.BooksView')
    @patch('src.controllers.books.BooksService')
    @patch('src.controllers.books.BooksModel')
    def test_books_controller__model_create_raw_dataframe(self, mock_books_model, mock_books_service, mock_books_view):
        mock_books_model_instance = mock_books_model.return_value
        mock_books_model_instance.check_raw_content.return_value = False
        self.controller.run()
        mock_books_model_instance.create_raw_dataframe.assert_called_once()

    @patch('src.controllers.books.BooksView')
    @patch('src.controllers.books.BooksService')
    @patch('src.controllers.books.BooksModel')
    def test_books_controller__model_get_books_title(self, mock_books_model, mock_books_service, mock_books_view):
        mock_books_model_instance = mock_books_model.return_value
        self.controller.run()
        mock_books_model_instance.get_books_title.assert_called_once()

    @patch('src.controllers.books.BooksView')
    @patch('src.controllers.books.BooksService')
    @patch('src.controllers.books.BooksModel')
    def test_books_controller__model_get_books_title_with_exception(self, mock_books_model, mock_books_service, mock_books_view):
        mock_books_model_instance = mock_books_model.return_value
        mock_books_model_instance.get_books_title.side_effect = Exception('Error')
        with self.assertRaises(Exception):
            self.controller.run()
        mock_books_model_instance.get_books_title.assert_called_once()

    @patch('src.controllers.books.BooksView')
    @patch('src.controllers.books.BooksService')
    @patch('src.controllers.books.BooksModel')
    def test_books_controller__model_get_book(self, mock_books_model, mock_books_service, mock_books_view):
        mock_books_model_instance = mock_books_model.return_value
        self.controller.run()
        mock_books_model_instance.get_book.assert_called_once()

    @patch('src.controllers.books.BooksView')
    @patch('src.controllers.books.BooksService')
    @patch('src.controllers.books.BooksModel')
    def test_books_controller__model_get_book_with_exception(self, mock_books_model, mock_books_service, mock_books_view):
        mock_books_model_instance = mock_books_model.return_value
        mock_books_model_instance.get_book.side_effect = Exception('Error')
        with self.assertRaises(Exception):
            self.controller.run()
        mock_books_model_instance.get_book.assert_called_once()

    @patch('src.controllers.books.BooksView')
    @patch('src.controllers.books.BooksService')
    @patch('src.controllers.books.BooksModel')
    def test_books_controller__model_get_book_author(self, mock_books_model, mock_books_service, mock_books_view):
        mock_books_model_instance = mock_books_model.return_value
        self.controller.run()
        mock_books_model_instance.get_book_author.assert_called_once()

    @patch('src.controllers.books.BooksView')
    @patch('src.controllers.books.BooksService')
    @patch('src.controllers.books.BooksModel')
    def test_books_controller__model_get_book_author_with_exception(self, mock_books_model, mock_books_service, mock_books_view):
        mock_books_model_instance = mock_books_model.return_value
        mock_books_model_instance.get_book_author.side_effect = Exception('Error')
        with self.assertRaises(Exception):
            self.controller.run()
        mock_books_model_instance.get_book_author.assert_called_once()

    @patch('src.controllers.books.BooksView')
    @patch('src.controllers.books.BooksService')
    @patch('src.controllers.books.BooksModel')
    def test_books_controller__service_create_word_cloud(self, mock_books_model, mock_books_service, mock_books_view):
        mock_books_service_instance = mock_books_service.return_value
        self.controller.run()
        mock_books_service_instance.create_word_cloud.assert_called_once()

    @patch('src.controllers.books.BooksView')
    @patch('src.controllers.books.BooksService')
    @patch('src.controllers.books.BooksModel')
    def test_books_controller__service_create_word_cloud_with_exception(self, mock_books_model, mock_books_service, mock_books_view):
        mock_books_service_instance = mock_books_service.return_value
        mock_books_service_instance.create_word_cloud.side_effect = Exception('Error')
        with self.assertRaises(Exception):
            self.controller.run()
        mock_books_service_instance.create_word_cloud.assert_called_once()
