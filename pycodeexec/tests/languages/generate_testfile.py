import json

from pycodeexec.languages import LANGUAGES

FILENAME = "./print_statements.json"

if __name__ == "__main__":
    with open(FILENAME) as fp:
        language_print_statements = json.load(fp)

    for language in LANGUAGES:
        if language not in language_print_statements:
            language_print_statements[language] = "Hello, World!"

    with open(FILENAME, "w") as fp:
        json.dump(language_print_statements, fp, indent=2)