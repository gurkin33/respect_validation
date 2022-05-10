# Custom rules

You can also create and use your own rules and exceptions.

To create a rule, you need to create a class that inherits the AbstractRule class
and add package (with the rule module) to `Factory`. When the rule is called the logic inside the
validate method will be executed. I will be more clear in example.

Start with creation of a rule. Below you can see a class of a new custom rule:

```python
from respect_validation.Rules.AbstractRule import AbstractRule


class CustomRule(AbstractRule):

    def validate(self, input_val) -> bool:

        return input_val == 'Hello custom rule!'
```
!!! attention
    <ins><b>Names of module (file name) and class of rule must be the same</b></ins> 
    (for example, the name of module CustomRule.py, then the name of class is CustomRule). 
    Name are case-sensitive and <ins><b>must start with upper letter</b></ins> 
    (<b>C</b>ustomRule - ✅ , <b>c</b>ustomRule - ❌ ).

Each rule must have an Exception to go with it. Exceptions should be named
with the name of the rule followed by the word Exception. The process of creating
an Exception is similar to creating a rule but there are no methods in the
Exception class. Instead, you create one static property that includes an
array with the information below:

```python
from respect_validation.Exceptions import ValidationException


class CustomRuleException(ValidationException):

    _default_templates = {
        'default': {
            'standard': 'Validation message if Something fails validation.'
        },
        'negative': {
            'standard': 'Validation message if the negative of Something is called and fails validation.'
        }
    }
```

!!! info
    There are two modes in exception messages **default** and **negative**. Default mode is active while 
    usual use. Negative mode is active when a rule inside [`Not`](rules/Not.md) rule.

So in the end, the folder structure for your Rules and Exceptions should look
something like the structure below. If you understand how it works, then you can use your own structure 😎.

```
Custom
│-- __init__.py
│
│-- Rules
│   │-- __init__.py
│   │-- CustomRule.py
│   │-- CustomRule1.py
│   │-- CustomRule2.py
│   │-- CustomRule3.py
│   `-- ...
`-- Exceptions
    │-- __init__.py
    │-- CustomRuleException.py
    │-- CustomRule1Exception.py
    │-- CustomRule2Exception.py
    │-- CustomRule3Exception.py
    `-- ...
```

All classes in Validation are creating by the `Factory` class. If you want
Validation to execute your rule (or rules) in the chain, you must add path (paths) of your packages to the
default `Factory`.

```python
from respect_validation import Validator as v
from respect_validation.Factory import Factory


Factory.add_rules_packages('Custom.Rules')
Factory.add_exceptions_packages('Custom.Exceptions')

v.customRule().validate('Hello custom rule!')
```

## Add arguments (attributes/parameters) to custom rule

To add arguments to custom rule please use next example:

```python
from respect_validation.Rules.AbstractRule import AbstractRule


class CustomRule(AbstractRule):
    
    _class_parameter: bool = False
    
    def __init__(self, new_argument: bool):
        super().__init__()
        self._class_parameter = new_argument

    def validate(self, input_val) -> bool:
        if self._class_parameter:
            return input_val == 'Hello custom rule!'
        else:
            False
```
!!! attention
    Don't forget to add `super().__init__()`, else you may have problems.

Now you can write rule in this way:
```python
v.customRule(new_argument=True).validate('Hello custom rule!')
```

## Add parameters for exception messages

You can set parameters in rule class and then use these parameters in exception message. By default, all rules 
has parameter __name__ and for custom rule it will be equals to input value. For example, we set parameter `my_name` 
in the rule below:
```python
from respect_validation.Rules.AbstractRule import AbstractRule


class CustomRule(AbstractRule):

    def validate(self, input_val) -> bool:
        my_name = 'Alexey Mochalin'
        #  please use method below to set parameter:
        self.set_param('my_name', my_name)
        return input_val == 'Hello World!'
```

We use this parameter in exception message:

```python
from respect_validation.Exceptions import ValidationException


class CustomRuleException(ValidationException):

    _default_templates = {
        'default': {
            'standard': 'Rule checked {name} and {my_name} thinks it should be equal to "Hello World!"'
        },
        'negative': {
            'standard': 'Rule checked {name} and {my_name} thinks it should NOT be equal to "Hello World!"'
        }
    }
```

Now we can try what we have created:

```python
from respect_validation.Factory import Factory
from respect_validation import Validator as v
from Custom.Exceptions.CustomRuleException import CustomRuleException


Factory.add_rules_packages('Custom.Rules')
Factory.add_exceptions_packages('Custom.Exceptions')

try:
    v.customRule().check('Hello custom rule!')
except CustomRuleException as cre:
    print(cre.get_message())

print("\nAnd for negative case:\n")
try:
    v.Not(v.customRule()).check('Hello World!')
except CustomRuleException as cre:
    print(cre.get_message())
```

Here is the output:

```
Rule checked "Hello custom rule!" and Alexey Mochalin thinks it should be equal to "Hello World!"

And for negative case:

Rule checked "Hello World!" and Alexey Mochalin thinks it should NOT be equal to "Hello World!"
```