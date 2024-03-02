from unittest.mock import patch, MagicMock
from src.services.books import BooksService


class TestBooksService():
    @patch(
        'src.services.books.WordCloud',
        return_value=MagicMock()
    )
    def test_books_service__transform(self, mock_word_cloud, raw_content_df_fixture):
        book_service = BooksService(raw_content_df_fixture)
        book_service.create_word_cloud()
        assert book_service._data.schema != raw_content_df_fixture.schema
