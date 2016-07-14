from nltk.corpus import stopwords


class Stopwords:
    def __init__(self):
        print("inside stopwords removal")

    def remove_all_stopwords(self,sentence):
        """
        revoving all stopwords from sentence
        :return: the sentence after revoving the stop words
        """

        # choosing the lexicon of english stop words
        stops=set(stopwords.words("english"))
        # spliting the sentence into word token
        sentence_tokens=sentence.split()
        # looping the sentence token and removing all the stop words from the sentence
        for token in sentence_tokens:
            if token in stops:
                sentence_tokens.remove(token)

        # rejoining the token to form sentence without stopwords
        new_sentence = ' '.join(str(s) for s in sentence_tokens)
        return new_sentence


# stopword=Stopwords()
# print(stopword.remove_all_stopwords("This would create first object of New Zealand"))