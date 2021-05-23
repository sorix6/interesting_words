from text_processing.processor import Processor


class TestProcessor:

    def test_interesting_words(self):
        """ Ensure the most interesting words can be retrieved.

        :raises AssertionError:
        :return void:
        """
        input_tokens = [
            'This is a sentence',
            'That is another sentence',
            'This sentence and another thing'
        ]

        assert {'sentence': 3, 'another': 2} == Processor.interesting_words(input_tokens, 2)
