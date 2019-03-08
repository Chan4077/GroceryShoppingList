from os import path


class Utils:
    @staticmethod
    def get_file_ext(filepath) -> str:
        """
        Retrieves the file extension from a file path
        :param filepath: The file path
        :return: The file extension
        """
        return path.splitext(filepath)[1][1:]

    @staticmethod
    def get_file_name(filepath) -> str:
        """
        Retrieves the file name from a file path
        :param filepath: The file path
        :return: The file name
        """
        return path.basename(filepath)