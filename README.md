## Multi agent conversations

### Install LM studio on local Windows or Mac

    https://lmstudio.ai/

### Install conda
    https://conda.io/projects/conda/en/latest/user-guide/getting-started.html

### Setup AutoGen
Create conda environment

    conda create -n autogen python=3.11
    conda env list
    conda activate autogen

Install AutoGen

    pip install pyautogen


### Run code 
python ./multi-agent-conversation.py


###  Sample Outcome
Note: Outcome will vary based on your model, temperature and other settings

    lead_developer_agent (to chat_manager):

    Write a python function code to add two integer numbers.
    Also write unit test case for the function.

    --------------------------------------------------------------------------------
    developer_agent (to chat_manager):

    Here's the Python function:
    ```python
    def add_two_numbers(a, b):
        return a + b
    ```
    And here is a possible unit test:
    ```python
    import unittest

    class TestAddTwoNumbers(unittest.TestCase):
        def test_add_two_numbers(self):
            self.assertEqual(add_two_numbers(1, 1), 2)
            self.assertEqual(add_two_numbers(-1, -3), -2)
            self.assertEqual(add_two_numbers(0, 0), 0)
            with self.assertRaises(TypeError):
                add_two_numbers("1", 2)
    ```
    This test case checks that the function `add_two_numbers` correctly adds two integer numbers and handles some basic edge cases, as well as checking if it raises an error when non-integer types are passed.

    --------------------------------------------------------------------------------
    lead_developer_agent (to chat_manager):

    Your code looks correct for both the add_two_numbers function and the test case. The function takes in two arguments and returns their sum. The test case checks that the function works correctly with multiple inputs, including negative numbers, and also tests that it raises a TypeError when a non-integer type is passed as an argument. This is a good way to ensure that your code is correct and handles expected edge cases.

    --------------------------------------------------------------------------------
    developer_agent (to chat_manager):

    Thank you! I'm glad my solution met your expectations. If you have any more questions or need further assistance, feel free to ask. I'll be happy to help.
