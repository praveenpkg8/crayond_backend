class FileNotFoundException(Exception):

    def __init__(self, value):
        self.error_message = value


class FileNotSelectedException(Exception):

    def __init__(self, value):
        self.error_message = value
