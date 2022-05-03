# KeyValue

- `keyValue(compared_key: str, rule_name: str, base_key: str)`

Performs validation of `compared_key` using the rule named on `rule_name` with
`base_key` as base.

Sometimes, when validating arrays, the validation of a key value depends on
another key value and that may cause some ugly code since you need the input
before the validation, making some checking manually:

```python
data = {
    'password': 'qwerty',
    'password_confirmation': 'qwerty'
}
v.key('password', v.notEmpty()).validate(data)
v.key('password_confirmation', v.equals(data.get('password', None))).validate(data)
```

The problem with the above code is because you do not know if `password` is a
valid key, so you must check it manually before performing the validation on
`password_confirmation`.

The `keyValue()` rule makes this job easier by creating a rule named on
`rule_name` passing `base_key` as the first argument of this rule, see an example:

```python
v.keyValue('password_confirmation', 'equals', 'password').validate(data)
```

The above code will result on `True` if _`data['password_confirmation']` is
[equals](Equals.md) to `data['password']`_.

This rule will invalidate the input if `compared_key` or `base_key` don't exist,
or if the rule named on `rule_name` could not be created (or don't exist).

When using `claim()` or `check()` methods and the rule do not pass, it overwrites
all values in the validation exceptions with `base_key` and `compared_key`.

```python
data = {
    'password': 'qwerty123123',
    'password_confirmation': 'qwerty'
}
try:
    v.keyValue('password_confirmation', 'equals', 'password').check(data)
except ValidationException as exception:
    print(exception)
```

The above code may generate the message:

```
password_confirmation must be equal to password
```

## Categorization

- Arrays
- Nesting

## Changelog

Version | Description
--------|-------------
  1.0.0 | Created

***
See also:

- [Equals](Equals.md)
- [Key](Key.md)
- [KeySet](KeySet.md)