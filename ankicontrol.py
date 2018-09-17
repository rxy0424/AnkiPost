import requests


class AbstractAnkiControl:
    def add_deck(self, word_info: dict):
        pass


class AnkiControlLocal(AbstractAnkiControl):
    def add_deck(self, word_info: dict):
        m_data = {
            'action': 'addNote', 'params': {
                'note': {
                    'fields': {
                        'expression': word_info['content'],
                        'glossary': word_info['definition'],
                        'sentence': word_info['sentence'],
                        'reading': word_info['pronunciation']
                    },
                    'tags': {},
                    'deckName': 'paper::paperWords',
                    'modelName': 'Facebook'
                }
            }
        }
        r = requests.post('http://127.0.0.1:8765', json=m_data)
        r.status_code
