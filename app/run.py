import logging
import os

from text_processing.word_searcher import WordSearcher
from text_processing import settings # noqa

LOGGER = logging.getLogger(__name__)


def read_files(folder):
    """ Return the contents of all files in folder.

    :param str folder:
    :return list(str):
    """
    texts = []

    for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename)
        with open(filepath, 'r') as file:
            texts.append(file.read())

    return texts


if __name__ == '__main__':

    texts = read_files('/usr/src/files')

    results = WordSearcher(texts).process_documents(2)

    for word, info in results.items():
        LOGGER.info('"%s" appeared %s times in:' % (word, info['count']))

    LOGGER.info(results)
