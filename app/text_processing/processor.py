from collections import Counter

from text_processing import tasks

class Processor:

    @classmethod
    def interesting_words(cls, sentences, counter = 5):
        """ Return top N words and their most frequent appearences in the given documents.

        :param list(str) documents:
        :param int counter:
        :return dict:
        """
        sentences_of_tokens = cls._process_text(sentences)

        counts = Counter([token for tokens in sentences_of_tokens for token in tokens])

        ordered_counts = {key: value for key, value in sorted(counts.items(), key=lambda item: item[1], reverse = True)}

        return dict(list(ordered_counts.items())[:counter])

    @staticmethod
    def _process_text(sentences):
        """ Process the given text using the pre-processing tasks.

        :param list(str) sentences:
        :return list(list(str)):
        """
        transformed_text = tasks.ToLowercase().transform(sentences)
        transformed_text = tasks.RemovePunctuation().transform(transformed_text)
        transformed_text = tasks.SplitToTokens().transform(transformed_text)

        return tasks.RemoveStopWords().transform(transformed_text)
