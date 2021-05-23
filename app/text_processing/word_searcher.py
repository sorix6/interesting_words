from text_processing.processor import Processor
from text_processing import tasks


class WordSearcher:

    def __init__(self, documents):
        """ Constructor.

        :param list(str) documents:
        :return void:
        """
        self.documents = documents

    def process_documents(self, counter = 5):
        """ Return the location of the most interesting words in the given documents.

        :param int counter:
        :return dict:
        """
        sentences_by_document = []
        for document in self.documents:
            sentences_by_document.append(tasks.SplitToSentences().transform(document))

        interesting_words = Processor.interesting_words(
            [sentence for sentences in sentences_by_document for sentence in sentences],
            counter
        )

        results = {}

        for word, count in interesting_words.items():
            results[word] = {'count': count}
            for document_index, sentences in enumerate(sentences_by_document):
                matches = self._search_word_in_document(sentences, word)

                if matches:
                    results[word][document_index] = matches

        return results

    @staticmethod
    def _search_word_in_document(sentences, word):
        """ Return the positions of the word in the given list of sentences.

        :param list(str) sentences:
        :param str word:
        :return set:
        """
        matches = []
        for index, sentence in enumerate(sentences):
            if word in sentence:
                matches.append(index)

        return matches
