from stemming import Stemming
from utilities import Stopwords, TaggingPOS
import gensim


class ExtractKeywords:
    
    __initString__=''
    __stopwordsRemovedString__=''
    __lemmatizedString__=''


    def __init__(self,string):
        self.__initString__ = string
        print("inside extracted keywords")


    def extracted_keywords(self):
        """
        extract keywords and send the list of keywords
        :param string:
        :return: list of keywords
        """

        # 1.stopwords revoval
        stopword = Stopwords()
        __stopwordsRemovedString__ = stopword.remove_all_stopwords(self.__initString__)
        print(__stopwordsRemovedString__)

        # 2.lemmatization
        lemmatization = Stemming()
        __lemmatizedString__ = lemmatization.use_snowball_stemmer(self.__stopwordsRemovedString__)
        print(__lemmatizedString__)

    # 3.getting the pos for the sentences
    def extract_candidate_chunks(self,text, grammar=r'KT: {(<JJ>* <NN.*>+ <IN>)? <JJ>* <NN.*>+}'):
        """ Extract candidate chunks from the sentence given and follow the pattern listed """
        import itertools, nltk, string
        print('Inside extract_candidate_chunks ...')

        # exclude candidates that are stop words or entirely punctuation
        punct = set(string.punctuation)
        stop_words = set(nltk.corpus.stopwords.words('english'))

        # tokenize, POS-tag, and chunk using regular expressions and creating the
        # chunk.RegexpParser with 1 stages:
        #     RegexpChunkParser with 1 rules:
        #            <ChunkRule: '(<JJ>* <NN.*>+ <IN>)? <JJ>* <NN.*>+'>
        # see parsing vs chunking @http://nltk.sourceforge.net/doc/en/ch06.html
        chunker = nltk.chunk.regexp.RegexpParser(grammar)

        # this will tag the word with probable pos
        tagged_sents = nltk.pos_tag_sents(nltk.word_tokenize(sent) for sent in nltk.sent_tokenize(text))

        # chunks the data in IOB-tags which means tagged with one of three special chunk tags,
        # I (inside), O (outside), or B (begin)
        all_chunks = list(itertools.chain.from_iterable(nltk.chunk.tree2conlltags(chunker.parse(tagged_sent))for tagged_sent in tagged_sents))

        # join constituent chunk words into a single chunked phrase
        # 1. all_chunks is like (word,pos,chunk) and we are neglecting the words which are outside the in the IOB tags
        # 2. groupby with chunks
        # 3. Lower case the chunks and join B and I
        candidates = [' '.join(word for word, pos, chunk in group).lower()
            for key, group in itertools.groupby(all_chunks, lambda chunk: chunk != 'O') if key]
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
        # return all the list of chunks after removing all the stopwords
        return [cand for cand in candidates
                if cand not in stop_words and not all(char in punct for char in cand)]


    def extract_candidate_words(self,text, good_tags=set(['JJ','JJR','JJS','NN','NNP','NNS','NNPS'])):
        """ Here will get all the words which are eligigle for keywords """
        import itertools, nltk, string
        print('Inside extract_candidate_words')

        # exclude candidates that are stop words or entirely punctuation
        # 1. Getting the punctuation() list and storing
        # 2. Getting all the stopwords list and storing
        punct = set(string.punctuation)
        stop_words = set(nltk.corpus.stopwords.words('english'))

        # tokenize and POS-tag words
        # 1. tokenizing the string and an array is sent 
        # 2. the string is splits the token into words
        # 3. attach pos-tag to each and every word 
        tagged_words = itertools.chain.from_iterable(nltk.pos_tag_sents(nltk.word_tokenize(sent) for sent in nltk.sent_tokenize(self.__initString__)))

        # filter on certain POS tags and lowercase all words
        # 1. Iterate all word and tags and lower-case 
        # 2. Then qualify only the those tags which are there in the good_tags and
        #       check whether it is not present in the Stopwords
        # 3. And also remove the punctuation()
        candidates = [word.lower() for word, tag in tagged_words
                    if tag in good_tags and word.lower() not in stop_words
                    and not all(char in punct for char in word)]

        return candidates

    def score_keyphrases_by_tfidf(self,texts, candidates='chunks'):
        import  nltk,gensim
        from sklearn.feature_extraction.text import CountVectorizer
    
        # extract candidates from each text in texts, either chunks or words
        if candidates == 'chunks':
            boc_texts = [self.extract_candidate_chunks(text) for text in texts]
        elif candidates == 'words':
            boc_texts = [self.extract_candidate_words(text) for text in texts]

        for boc_text in boc_texts:
            print(boc_text)

        # for boc_text in boc_texts:
        #     print(boc_text)
        #
        # # sklearn
        # vec = CountVectorizer(min_df=1, stop_words=None, vocabulary=boc_texts)
        # X = vec.fit_transform(self.__initString__)
        # vocabs = vec.get_feature_names()
        #
        # for cocab in vocabs:
        #     print(cocab)
        #
        # # id2word = dict([(i, s) for i, s in enumerate(vec.get_feature_names())])
        # # vocabulary = boc_texts

        # make gensim dictionary and corpus
        dictionary = gensim.corpora.Dictionary(boc_texts)
        corpus = [dictionary.doc2bow(boc_text) for boc_text in boc_texts]
        # transform corpus with tf*idf model
        tfidf = gensim.models.TfidfModel(corpus)
        corpus_tfidf = tfidf[corpus]


        
        return corpus_tfidf, dictionary



# tag = TaggingPOS()
# text_with_tag = tag.find_the_country_name("This would create first object of New Zealand")

str="It was the feeling that induces a volunteer recruit to spend his last penny on drink, and a drunken man to smash mirrors or glasses for no apparent reason and knowing that it will cost him all the money he possesses: the feeling which causes a man to perform actions which from an ordinary point of view are insane, to test, as it were, his personal power and strength, affirming the existence of a higher, nonhuman criterion of life."
keyword=ExtractKeywords(str)
# keyword.extract_candidate_chunks(str)
# keyword.extract_candidate_words(str)
corpus_tfidf,dict = keyword.score_keyphrases_by_tfidf(str)
for items in corpus_tfidf:
    for item in items:
        print(item)

