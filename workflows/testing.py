import unittest
import json
import subprocess

def input_recomande(input_set: list) -> str:
    input_set = f"{input_set[0]} {input_set[1]}\n{input_set[2]} {input_set[3]}\n"
    return input_set

with open('workflows/test_data.json', 'r') as file:
    test_cases = json.load(file)

name_test_file = input('the full name of the file to be tested: ')

class Testing(unittest.TestCase):
    def setUp(self):
        self.test_cases = test_cases

    def testing(self):
        for input_set in self.test_cases:
            input_value = input_recomande(input_set["input"])
            expected_output = input_set["expected_output"]

            with self.subTest(input_valuse=input_value):
                result = subprocess.run(
                    ['/usr/bin/python3', name_test_file],
                    input=input_value,
                    capture_output=True,
                    text=True,
                )
                output = result.stdout.strip()
                self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()