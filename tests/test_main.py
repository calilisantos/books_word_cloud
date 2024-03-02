from src.main import Main
from unittest.mock import patch


class TestMain():
    @patch(
        'src.controllers.books.BooksController.__init__',
        return_value=None
    )
    @patch('src.controllers.books.BooksController.run')
    def test_run(
        self,
        mock_books_controller,
        mock_books_controller_run,
    ):
        main = Main()
        main.run()
        mock_books_controller_run.assert_called
