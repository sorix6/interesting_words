from text_processing import tasks


class TestTasks:

    def test_split_to_sentences(self):
        """ Ensure a given text is correctly split into sentences.

        :raises AssertionError:
        :return void:
        """
        input_text = 'This is a text. This is a sentence! Is it?'

        assert ['This is a text.', 'This is a sentence!', 'Is it?'] == tasks.SplitToSentences().transform(input_text)

    def test_lowercase(self):
        """ Ensure text is correctly transformed to lowercase.

        :raises AssertionError:
        :return void:
        """
        input_text = ['This is A test.', 'FOr lowerCase!']

        assert ['this is a test.', 'for lowercase!'] == tasks.ToLowercase().transform(input_text)

    def test_remove_puntuation(self):
        """ Ensure punctuation is correctly removed.

        :raises AssertionError:
        :return void:
        """
        sentences = ['This is, a text.', 'This is : text!', 'Is it ?']

        assert ['This is a text', 'This is  text', 'Is it '] == tasks.RemovePunctuation().transform(sentences)

    def test_split_to_tokens(self):
        """ Ensure text can be correctly split into tokens.

        :raises AssertionError:
        :return void:
        """
        input_sentences = ['split this into tokens']

        assert [['split', 'this', 'into', 'tokens']] == tasks.SplitToTokens().transform(input_sentences)

    def test_remove_stop_words(self):
        """ Ensure stop words are correctly removed.

        :raises AssertionError:
        :return void:
        """
        input_sentences = [['this', 'is',  'a', 'stopword']]

        assert [['stopword']] == tasks.RemoveStopWords().transform(input_sentences)
