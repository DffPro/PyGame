import json


class ScoreStorage:
    """Сохраняет и загружает рекорд из json-файла."""

    def __init__(self, path):
        self._path = path

    def load(self):
        try:
            with open(self._path, 'r') as file:
                return json.load(file)['high_score']
        except (FileNotFoundError, ValueError, KeyError):
            return 0

    def save(self, high_score):
        with open(self._path, 'w') as file:
            json.dump({'high_score': high_score}, file)