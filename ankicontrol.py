import requests


class AbstractAnkiControl:
    def __init__(self, deck_name="", model_name=""):
        self.deckName = deck_name
        self.modelName = model_name

    def add_deck(self, word_info: dict):
        pass


class AnkiControlLocal(AbstractAnkiControl):
    def __init__(self, deck_name="", model_name=""):
        super(AnkiControlLocal, self).__init__(deck_name, model_name)

    def add_deck(self, word_info: dict, tags: dict = {}):
        m_data = {
            'action': 'addNote', 'params': {
                'note': {
                    'fields': word_info,
                    'tags': tags,
                    'deckName': self.deckName,
                    'modelName': self.modelName
                }
            }
        }
        requests.post('http://127.0.0.1:8765', json=m_data)
