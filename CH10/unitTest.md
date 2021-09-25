## 第十一章 测试代码

在本章中将会学习如何使用Python模块 `unittest`中的工具来测试代码。

### 单元测试和测试用例

**单元测试**用于合核实函数的某个方面没有问题。**测试用例**是一组单元测试，他们一道核实函数在各种情况下的行为都符合要求。

测试函数：

```python
// get_format_name.py
def get_format_name(first, last):
    full_name = f"{first} {last}"
    return full_name.title()
```

测试用例：

```python
// test_format_name.py
import unittest
from get_format_name import get_format_name


class NameTestCase(unittest.TestCase):
    def test_first_last_name(self):
        format_name = get_format_name('john', 'hans')
        self.assertEqual(format_name, 'John Hans')


if __name__ == '__main__':
    unittest.main()
```

首先导入模块`unittest`和要测试的函数 `get_format_name`。然后创建了一个名为`NameTest`的类，用于包含一系列针对 `get_format_name`的单元测试。这个类名可以随意命名，但这个类必须继承 `unittest.TestCase`类，这样Python才知道如何运行你编写的测试。

`NameTestCase`只包含一个方法，用于测试`get_fomat_name`的一个方面。将该方法命名为 `test_first_last_name()`。运行`test_format_name.py`时，**所有以test开头的方法都会自动运行**。

`assertEqual`是`unittest`类最有用的功能之一：**断言**方法。

### 测试类

前面是针对单个函数的测试，下面编写针对类的测试。

#### 常用的断言方法

|          方法           |        用途        |
| :---------------------: | :----------------: |
|    assertEqual(a, b)    |     核实a == b     |
|  assertNotEqual(a, b)   |     核实a != b     |
|      assertTrue(x)      |    核实x为True     |
|     assertFalse(x)      |    核实x为False    |
|  assertIn(item, list)   |  核实item在list中  |
| assertNotIn(item, list) | 核实item不在list中 |

一个要测试的类：

```python
class AnonymousSurvey:
    def __init__(self, question):
        self.question = question
        self.response = []

    def show_question(self):
        print(self.question)

    def store_response(self, new_response):
        self.response.append(new_response)

    def show_result(self):
        print("Survey result:")
        for response in self.response:
            print(f"- {response}")
```

测试用例：

```python
import unittest
from get_format_name import AnonymousSurvey


class NameTestCase(unittest.TestCase):
    def test_first_last_name(self):
        format_name = get_format_name('john', 'hans')
        self.assertEqual(format_name, 'John Hans')

    def test_store_single_response(self):
        question = 'How old are you?'
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('20')
        self.assertIn('20', my_survey.response)

    def test_store_three_response(self):
        question = 'what language did you first learn to sprak?'
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            my_survey.store_response(response)
        for response in responses:
            self.assertIn(response, my_survey.response)


if __name__ == '__main__':
    unittest.main()
```

#### setUp()

在前面的测试用例中，我们在每个测试方法中都创建了AnonymousSurvey实例，并且在每个方法中都创建了答案。unittest.TestCase类包含的方法`setUp()`让我们只需创建这些对象一次，就能在各个测试方法中使用。

如果在TestCase类中包含`setUp()`方法，Python将先运行它，再运行各个以test_开头的方法。这样在你编写的每个测试方法中，都可以使用在方法`setUp()`中创建的对象。

```python
import unittest
from get_format_name import AnonymousSurvey


class NameTestCase(unittest.TestCase):
    def setUp(self) -> None:
        question = 'what language did you first learn to sprak?'
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.response)

    def test_store_three_response(self):
        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.response)


if __name__ == '__main__':
    unittest.main()
```