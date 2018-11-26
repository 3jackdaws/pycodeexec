import unittest
import asynctest
from pycodeexec import Runner
import time
import json
from pycodeexec.util import time_this
from os import path
from pycodeexec.languages import LANGUAGES


def get_print_statements():
    with open(path.join(path.dirname(__file__), "print_statements.json")) as fp:
        return json.load(fp)


class TestExecutePrintStatement(unittest.TestCase):
    def test_languages_default(self):
        print_statements = get_print_statements()
        EXPECTED = "Hello, World!"
        print("Languages:")
        for language in LANGUAGES:
            print(language.upper())
            code = print_statements[language]
            runner = Runner(language)
            actual = runner.get_output(code).strip()
            self.assertEqual(EXPECTED, actual)


class TestExecuteAsyncPrintStatements(asynctest.TestCase):
    async def test_languages_default(self):
        from pycodeexec.asyncio import Runner
        print_statements = get_print_statements()
        EXPECTED = "Hello, World!"
        print("Languages:")
        for language in LANGUAGES:
            print(language.upper())
            code = print_statements[language]
            runner = Runner(language)
            await runner.is_ready()
            actual = (await runner.get_output(code)).strip()
            self.assertEqual(EXPECTED, actual)