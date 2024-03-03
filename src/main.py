from src.controllers.books import BooksController


class Main:
    def __init__(self) -> None:
        self._get_data = BooksController()

    def run(self) -> None:
        self._get_data.run()


if __name__ == '__main__':
    Main().run()
