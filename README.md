# respect_validation
[![Tests (pytest, flake8, mypy)](https://github.com/gurkin33/respect_validation/actions/workflows/tests.yml/badge.svg)](https://github.com/gurkin33/respect_validation/actions/workflows/tests.yml)
[![Code Coverage](https://img.shields.io/codecov/c/github/gurkin33/respect_validation?style=flat-square)](https://codecov.io/gh/gurkin33/respect_validation)

[![PyPI license](https://img.shields.io/pypi/l/respect-validation.svg?style=flat-square)](https://pypi.python.org/pypi/respect-validation/)
[![PyPI version respect_validation](https://img.shields.io/pypi/v/respect-validation.svg?style=flat-square)](https://pypi.org/project/respect-validation/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/respect-validation.svg?style=flat-square)](https://pypi.python.org/pypi/respect-validation/)

Python version of "[the most awesome validation engine for PHP](https://github.com/Respect/Validation)"

### [Documentation](https://gurkin33.github.io/respect_validation/)

### Installation

```bash
pip install respect-validation
```

<p align="center">
  <img src="docs/logo_schema_slim.png" />
</p>

PHP and Python have many differences that why this library has some small changes, but an awesome architecture was migrated without changes.

General description:

- Complex rules made simple: `v.numericVal().positive().between(1, 255).validate(some_variable)`.
- [Advanced reporting](https://gurkin33.github.io/respect_validation/feature-guide/#getting-all-messages-as-a-dict/) to show validation errors.
- [More than 130](https://gurkin33.github.io/respect_validation/list-of-rules/) (fully tested) validation rules.
- [Integration with Flask](https://gurkin33.github.io/respect_validation/flask%20integration/2_simple_flask/) example.

### Why is it great alternative to others?

- It is easy to make logical check in one line. You __can easily see logic
in chain of rules__. There are no addition classes, instances,
dictionaries, __there is only one chain of rules__ and it is
beautiful.
- There are logical operators inside, you can use them as usual rules.
You can easily set several validation chains and wrap them into
logical rule like `AnyOf` or `OneOf` (only one chain valid) or
`AllOf` or `When` (if ... then ... else) and so on. I hope you will
find this interesting.
- Any rule or chain of rules you can easily revert to negative result
with only one logical rule - `Not`.
- There are many of prebuilt rules. They will be useful for most of
general cases.
- You can easily create you own package of rules and use it when it is
needed.

### How to say thank you?

If you like this library please add star for initial library
"[the most awesome validation engine for PHP](https://github.com/Respect/Validation)".

Many thanks to Alexandre Gomes Gaigalas for beautiful architecture.
