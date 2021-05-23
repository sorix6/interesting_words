import abc
import re
import string

import spacy


class BaseTask(abc.ABC):

    @abc.abstractmethod
    def transform(self, X):
        """ Perform the task.
        """
        pass


class ToLowercase(BaseTask):

    def transform(self, X):
        """ Return the input texts in lowercase.

        :param str text:
        :return str:
        """
        return [sentence.lower() for sentence in X]

class SplitToSentences(BaseTask):

    NLP = spacy.load('en_core_web_sm')

    def transform(self, X):
        """ Split a given text into sentences and return a list containing the sentences.

        :param str text:
        :return list(str):
        """
        return [sent.text for sent in self.NLP(X).sents]

class RemovePunctuation(BaseTask):

    PUNCTUATION_PATTERN = re.compile(r'[^\w\s]')

    def transform(self, X):
        """ Remove punctuation from a given list of sentences.

        :param list(str) sentences:
        :return list(str):
        """
        return [self.PUNCTUATION_PATTERN.sub('', sentence) for sentence in X]


class SplitToTokens(BaseTask):

    def transform(self, X):
        """ Remove punctuation from a given list of sentences.

        :param list(str) sentences:
        :return list(str):
        """
        return [sentence.split() for sentence in X]

class RemoveStopWords(BaseTask):

    STOP_WORDS = {
        'a', 'and', 'at', 'for', 'in', 'into', 'is', 'of', 'or', 'the', 'this', 'that', 'to', 'where', 'when'
    }

    def transform(self, X):
        """ Remove stop words from a given list of sentences formatted as tokens.

        :param list(list(str)):
        :return list(list(str)):
        """
        return [
            [token for token in sentence_tokens if token not in self.STOP_WORDS]
            for sentence_tokens in X
        ]
