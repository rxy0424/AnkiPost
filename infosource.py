import requests


class InfoSource:
    def get_word_info(self, sentence: str, word: str) -> dict:
        """
        get word info from target source
        :param sentence: sentence that includes the word
        :param word: word than will be explained by source
        :return: dict content word's info
        """
        pass


class InfoSourceShanbay(InfoSource):
    def get_word_info(self, sentence: str, word: str) -> dict:
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
            word_info['expression'] = r_json['data']['content']
            word_info['glossary'] = r_json['data']['definition'].replace("\n", "<br>")
            word_info['reading'] = r_json['data']['pronunciation']
            word_info['sentence'] = sentence.replace("\n", " ").replace(word, "<b>" + word + "</b>").replace("- ", "")
        return word_info
