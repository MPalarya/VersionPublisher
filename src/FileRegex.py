
exclude_extensions = "pdb|db|obj|log|metagen|cache|config|manifest"
exclude_extensions = ".+\.(" + exclude_extensions + ")$"

START = "^"
END = "$"
ANY = ".?"
SOME = ".+"
DOT = "\."

NOTHING = "(?!x)x"
EVERYTHING = ".+\..+"



def any_file(prefix="", extension=""):
    """
    returns a regular expression matching files with a name prefix and/or an extension
    :param prefix: string that the file name begins with
    :param extension: string ".exe" or "exe" or multiple extensions pipelined as "exe|ini"
    :return: string
    """
    result = ""

    if len(prefix) == 0:
        result = SOME + DOT

    else:
        result = START + prefix + ANY + DOT

    if len(extension) == 0:
        result += ANY

    else:
        extension = extension.translate(None, '.')
        if '|' in extension:
            result += "(" + extension + ")" + END

        else:
            result += extension + END

    return result

#def file_extensions(extensions):
#    return "

print any_file()
print any_file(prefix="Dev")
print any_file(prefix="Dev", extension=".dll")
print any_file(prefix="Dev", extension=".dll|.ini")
print any_file(extension=".dll|.ini")