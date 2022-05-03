# Feature Guide

## import respect_validation

In most cases you need only Validator. It will be handy to import it just like one letter "v":

```python
from respect_validation import Validator as v
```

## Simple validation

The Hello World validator is something like this:

```python
number = 123
v.numericVal().validate(number) #  true
```

## Chained validation

It is possible to use validators in a chain. Sample below validates a string
containing numbers and letters, no whitespace and length between 1 and 15.

```python
username_validator = v.alnum().noWhitespace().length(1, 15)
username_validator.validate('alganet') #  true
```

## Validating object attributes

Given this simple object:

```python
class User(object):
  pass

user = User()
user.name = 'Alexandre'
user.birthdate = datetime('1987-07-01', '%Y-%m-%d')
```

Is possible to validate its attributes in a single chain:

```python
#  "name" in between 1 to 32 symbols
#  "birthdate" older than 18 years old
user_validator = v.attribute('name', v.stringType().length(1, 32)). \
    attribute('birthdate',
              v.date().Max(datetime(datetime.now().year - 18, datetime.now().month, datetime.now().day)))
user_validator.validate(user)  # true
```

Validating dictionary is also possible using `v.key()`

Note that we used `v.stringType()` and `v.date()` in the beginning of the validator.
Although is not mandatory, it is a good practice to use the type of the
validated object as the first node in the chain.

## Validating dictionaries

Validating dict into another dict is also possible using [Key](rules/Key.md).

If we got the dict below:

```python
data = {
    'parentKey': {
        'field1': 'value1',
        'field2': 'value2',
        'field3': True,
    }
}
```

Using the next combination of rules, we can validate child keys.

```python
v.key(
    'parentKey',
    v.key('field1', v.stringType()).\
        key('field2', v.stringType()).\
        key('field3', v.boolType())
    )\
    .claim(data) # You can also use check() or validate()
```

## Input optional

If you want to treat a value as optional you can use `v.optional()` rule:

```python
v.alpha().validate('')  # false input required
v.alpha().validate(None)  # false input required
v.optional(v.alpha()).validate('')  # true
v.optional(v.alpha()).validate(None)  # true
```

By _optional_ we consider `None` or an empty string (`''`).

See more on [Optional](rules/Optional.md).

## Negating rules

You can use the `v.Not()` (IMPORTANT to type with upper N) to negate any rule:

```python
v.Not(v.intVal()).validate(10)  # false, input must not be integer
```

## Validator reuse

Once created, you can reuse your validator anywhere. Remember `username_validator`?

```python
username_validator.validate('respect');            //true
username_validator.validate('alexandre gaigalas'); // false
username_validator.validate('#$%');                //false
```

## Exception types

- `Exception`:
  - All exceptions implement this interface;
- `ValidationException`:
  - Implements the `Exception` interface
  - Raise when the `check()` fails
  - All validation exceptions extend this class
  - Available methods:
    - `get_message()`;
    - `update_mode(mode)`;
    - `update_template(template)`;
- `NestedValidationException`:
  - Extends the `ValidationException` class
  - Usually thrown when the `claim()` fails
  - Available methods:
    - `get_full_message()`;
    - `get_messages()`;

## Informative exceptions

When something goes wrong, Validation can tell you exactly what's going on. For this,
we use the `claim()` method instead of `validate()`:

```python
from respect_validation.Exceptions import NestedValidationException
try:
    username_validator.claim('really messed up screen#name');
except NestedValidationException as exception:
   print(exception.get_full_message())
```

The printed message is exactly this, as a nested Markdown list:

```no-highlight
- All of the required rules must pass for "really messed up screen#name"
  - "really messed up screen#name" must contain only letters (a-z) and digits (0-9)
  - "really messed up screen#name" must not contain whitespace
  - "really messed up screen#name" must have a length between 1 and 15
```

## Getting all messages as a dict

If you want to get all the messages as a dict you can use `get_messages()` for
that. The `get_messages()` method returns an array with all the messages.

```python
try:
    username_validator.claim('really messed up screen#name');
except NestedValidationException as exception:
    print(exception.get_messages())
```

The `get_messages()` returns an array in which the keys are the name of the
validators, or its reference in case you are using [Key](rules/Key.md) or
[Attribute](rules/Attribute.md) rule:

```no-highlight
{
  'alnum': ['"really messed up screen#name" must contain only letters (a-z) and digits (0-9)'], 
  'noWhitespace': ['"really messed up screen#name" must not contain whitespace'], 
  'length': ['"really messed up screen#name" must have a length between 1 and 15']
}
```

## Custom messages

Getting messages as a dict is fine, but sometimes you need to customize them
in order to present them to the user. This is possible using the `get_messages()`
method as well by passing the templates as an argument:

```python
try:
    username_validator.claim('really messed up screen#name')
except NestedValidationException as exception:
    print(exception.get_messages({
            'alnum': '{{name}} must contain only letters and digits',
            'noWhitespace': '{{name}} cannot contain spaces',
            'length': '{{name}} must not have more than 15 chars',
        })
    )
```

For all messages, the `{{name}}` variable is available for templates. If you do
not define a name it uses the input to replace this placeholder.

The result of the code above will be:

```no-highlight
{
  'alnum': ['{name} must contain only letters and digits'], 
  'noWhitespace': ['{name} cannot contain spaces'], 
  'length': ['{name} must not have more than 15 chars']
}
```

Note that `get_message()` will only return a message when the specific validation
in the chain fails.

## Validator name

On `v.attribute()` and `v.key()`, `{{name}}` is the attribute/key name. For others,
is the same as the input. You can customize a validator name using:

```python
v.dateTime('%Y-%m-%d').between('1980-02-02', '2022-04-29').setName('Member Since');
```

## Validation methods

We've seen `validate()` that returns true or false and `claim()` that throws a complete
validation report. There is also a `check()` method that returns an Exception
only with the first error found:

```python
from respect_validation.Exceptions import ValidationException
try:
    username_validator.check('really messed up screen#name')
except ValidationException as exception:
    print(exception.get_message())
```

Message:

```no-highlight
"really messed up screen#name" must contain only letters (a-z) and digits (0-9)
```