from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import EnglishStemmer
from nltk.stem.lancaster import LancasterStemmer

class Stemming:
    def __init__(self):
        print("inside stepping of words")

    def use_porter_stemmer(self,word):
        """
        return stemmed words used porter algorithm
        :param words:
        :return:
        """
        porterStemmer=PorterStemmer()
        stemmed_word= porterStemmer.stem(word)
        return stemmed_word

    def use_snowball_stemmer(self,word):
        """
        return stemmed words used snowball algorithm
        :param word:
        :return:
        """
        englishStemmer=EnglishStemmer()
        stemmed_word= englishStemmer.stem(word)
        return stemmed_word

    def use_lancaster_stemmer(self,word):
        """
        return stemmed words used lancaster algorithm
        :param word:
        :return:
        """
        lancasterStemmer=LancasterStemmer()
        stemmed_word=lancasterStemmer.stem(word)
        return stemmed_word



# testing
# stem = Stemming()
# word = stem.use_porter_stemmer("duable")
# print(word)
# word = stem.use_snowball_stemmer("duable")
# print(word)
# word = stem.use_lancaster_stemmer("duable")
# print(word)