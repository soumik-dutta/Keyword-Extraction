import nltk


class TaggingPOS:
    """ Responsible to tag Parts-of-speech to every words
    """

    def __init__(self):
        print("Inside Tagging POS")

    def convert_words_to_postag(self, sentence):
        """
        get the pos for words
        :param sentence:
        :type list of tuples
        :return:text_with_tag: list of dictionary
        """

        # get all the words as token and then find its parts of speech
        text = nltk.tokenize.word_tokenize(sentence)
        text_with_tag = nltk.pos_tag(text)

        # @print
        print(text_with_tag)
        return text_with_tag

    def n_gram_creator(self, sentence, gram):
        """
        generating n-grams
        :param sentence:
        :param gram:
        :return: list of the n-gram tuples
        """

        # get the generated n-grams
        generated_ngrams = list(nltk.ngrams(sentence.split(), gram))
        print(generated_ngrams)
        return generated_ngrams

    def find_the_country_name(self, sentence):
        """
        check wheather the words is a country name
        :param sentence:
        :return:
        """
        bi_gram = self.n_gram_creator(sentence, 2)
        for first, second in bi_gram:
            # checking whether the bigrams starts with capital letter
            if first[0].isupper() and second[0].isupper():
                print(first + ' ' + second)
                str = first + ' ' + second

                print(self.is_word_a_place(str))
        return ""

    def is_word_a_place(self, word):
        """
        check whether a word a place
        :param word:
        :return:
        """
        is_record_found = False
        # places.txt in the home directory
        file_output = open("lexicons/places.txt")
        for lines in file_output:
            if lines.strip() == word:
                is_record_found = True
                break
        return is_record_found
