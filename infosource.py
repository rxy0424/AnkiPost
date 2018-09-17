import requests


class InfoSource:
    def get_word_info(self, sentence: str, word: str):
        pass


class InfoSourceShanbay(InfoSource):
    def get_word_info(self, sentence: str, word: str):
        word_info = {}
        dict_usr = 'https://api.shanbay.com/bdc/search/?word='+word
        try:
            r = requests.get(dict_usr, timeout=5)
        except:
            return word_info

        r_json = r.json()
        if r_json['status_code'] == 1:
            print("no word find")
        else:
            word_info['content'] = r_json['data']['content']
            word_info['definition'] = r_json['data']['definition'].replace("\n", "<br>")
            word_info['pronunciation'] = r_json['data']['pronunciation']
            word_info['sentence'] = sentence.replace("\n", " ").replace(word, "<b>" + word + "</b>").replace("- ", "")
        return word_info
