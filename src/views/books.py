from src.configs import transform as transform_conf, view as view_conf
import streamlit as st


class BooksView:
    def __init__(self, options: list):
        self._select_options = options

    def set_title(self):
        return st.write(
            f'<h1><center>{view_conf.TITLE_CONTENT}</center></h1>',
            unsafe_allow_html=True
        )

    def set_selectbox(self):
        return st.selectbox(
            label=view_conf.SELECT_BOX_LABEL,
            options=self._select_options
        )

    def set_image(self):
        return st.image(
            transform_conf.WORDCLOUD_IMAGE_NAME,
            use_column_width=True
        )

    def set_book_title(self, title: str):
        return st.write(f'#### Book Title - {title}')

    def set_author(self, author: str):
        return st.write(f'#### Book Author - {author}')
