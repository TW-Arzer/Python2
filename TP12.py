from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QGridLayout, QLabel, QLineEdit, QListWidget, QPushButton, QWidget
from datetime import *
import sys
import requests
import tmdbsimple as tmdb

API_KEY = "YOUR_API_KEY"

# mostly copied from solutions


class TMDBSearchWidget(QWidget):
    DEFAULT_TITLE = "Recherche The Movie DB (film)"
    ILLUSTRATION_SIZE = 250

    def __init__(self):
        super().__init__()
        self.results = []

        grid = QGridLayout()
        grid.setSpacing(10)

        self.search_label = QLabel("Recherche film")
        grid.addWidget(self.search_label, 0, 0)

        self.search_edit = QLineEdit()
        grid.addWidget(self.search_edit, 0, 1, 1, 3)

        self.search_button = QPushButton("Rechercher")
        grid.addWidget(self.search_button, 0, 4)

        self.search_result_list = QListWidget()
        self.search_result_list.setMinimumWidth(300)
        grid.addWidget(self.search_result_list, 1, 0, 5, 2)

        self.title_label = QLabel("Titre")
        grid.addWidget(self.title_label, 1, 2)

        self.title_edit = QLineEdit()
        self.title_edit.setReadOnly(True)
        grid.addWidget(self.title_edit, 1, 3, 1, 2)

        self.directors_label = QLabel("Réalisateurs")
        grid.addWidget(self.directors_label, 2, 2)

        self.directors_edit = QLineEdit()
        self.directors_edit.setReadOnly(True)
        grid.addWidget(self.directors_edit, 2, 3, 1, 2)

        self.illustration_label = QLabel()
        self.illustration_label.setFixedWidth(int(self.ILLUSTRATION_SIZE / 3 * 2))

        self.illustration_label.setFixedHeight(self.ILLUSTRATION_SIZE)
        self.illustration_label.setScaledContents(True)
        grid.addWidget(self.illustration_label, 3, 3, 2, 2)

        self.search_button.clicked.connect(self.search)
        self.search_edit.textChanged.connect(self.update_window_title)

        self.search_result_list.itemSelectionChanged.connect(self.update_details)

        self.exit_button = QPushButton("Exit")
        grid.addWidget(self.exit_button, 6, 4)
        self.exit_button.clicked.connect(self.close)

        grid.setColumnStretch(0, 0)
        grid.setColumnStretch(1, 1)
        grid.setColumnStretch(2, 0)
        grid.setColumnStretch(3, 1)
        grid.setColumnStretch(4, 0)
        self.setLayout(grid)
        self.setGeometry(300, 300, 550, 350)
        self.setWindowTitle(self.DEFAULT_TITLE)
        self.show()

    def search(self):
        tmdb.API_KEY = API_KEY
        search = tmdb.Search()
        search.movie(query=self.search_edit.text())

        self.results = search.results
        self.search_result_list.clear()
        for film in self.results:
            try:
                release_date = datetime.strptime(film["release_date"], "%Y-%m-%d")
                year = str(release_date.year)
            except:
                year = "-"

            self.search_result_list.addItem(f"{film['title']} ({year}")
        self.title_edit.clear()
        self.directors_edit.clear()
        self.illustration_label.clear()

    def update_window_title(self):
        search_str = self.search_edit.text()
        if search_str == "":
            self.setWindowTitle(self.DEFAULT_TITLE)
        else:
            self.setWindowTitle(f"{self.DEFAULT_TITLE}: '{search_str}'")

    def update_details(self):
        for index in self.search_result_list.selectedIndexes():
            film = self.results[index.row()]
            movie = tmdb.Movies(film["id"])

            directors = ", ".join([director["name"] for director in movie.credits()["crew"]
                                   if director["job"] == "Director"])

            if film["poster_path"]:
                response = requests.get(f"https://image.tmdb.org/t/p/original{film['poster_path']}")
                film["image_data"] = response.content

                illustration = QPixmap()
                illustration.loadFromData(film["image_data"])
                self.illustration_label.setPixmap(illustration)
            else:
                self.illustration_label.clear()

            self.title_edit.setText(film["title"])
            self.directors_edit.setText(directors)
            break


if __name__ == '__main__':
    app = QApplication([])
    ex = TMDBSearchWidget()
    sys.exit(app.exec())
