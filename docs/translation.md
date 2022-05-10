# Translation

There are two type of translations available:

- One language
- Multi-language

## One language

In case of one language you prepare dictionary with translation and add it to `Factory`.

Example of all default messages for all default rules you can find 
[here](https://github.com/gurkin33/respect_validation/blob/1.2.0/bin/default_messages.json). Let's 
get messages for one rule and review them:

```json
{
  "positive": {
    "default": {
      "standard": "{name} must be positive"
    },
    "negative": {
      "standard": "{name} must not be positive"
    }
  }
}
```

Above we can see default messages for rule _Positive_, because we can see rule ID.

!!! info
    Rule ID is a name of rule class but fist letter in lower case. For example, class name _SomeCustomRule_, 
    then rule ID is _someCustomRule_.

This library has **two modes** for rule - **default** and **negative**. You can see the first mode (default) in most cases 
but if a rule inside `Not` rule, then the rule will switch to the second mode (negative).

Inside _modes_ you can find message **templates**. One or several message templates for rule can be.

!!! tip
    There is no need to translate all messages from 
    [provided dictionary](https://github.com/gurkin33/respect_validation/blob/1.2.0/bin/default_messages.json) 
    you can add rules which you want to use. If library cannot find related messages in 
    provided dictionary, then it will use default ones.

### Example

```python
from respect_validation import Validator as v, Factory
from respect_validation.Exceptions import NestedValidationException

# our translation dictionary with only one translation
translation = {
    "positive": {
        "default": {
          "standard": "Is {name} positive? I don't think so..."
        },
        "negative": {
          "standard": "Is {name} NOT positive? I don't think so..."
        }
    }
}

# set translation dict in the Factory
Factory.set_translation(translation)

try:
    v.numericVal().positive().claim('ggg')
except NestedValidationException as nve:
    print(nve.get_messages())
    print(nve.get_full_message())
```
Output

```text
# nve.get_messages()
{'numericVal': ['"ggg" must be numeric'], 'positive': ['Is "ggg" positive? I don\'t think so...']}

# nve.get_full_message()
- All of the required rules must pass for "ggg"
  - "ggg" must be numeric
  - Is "ggg" positive? I don't think so...
```

## Multi-language

It is similar to one language example but with some differences.

Let's start with dictionary. Now it has language key as a first layer of dict and inside it has 
language dictionary. 
!!! tip
    The same as for one language case - there is no need to translate all messages, you can add rules which 
    you want to use, "untranslated" rules will have default messages.

```json
{
  "en": {
    "positive": {
      "default": {
        "standard": "{name} must be positive"
      },
      "negative": {
        "standard": "{name} must not be positive"
      }
    }
  },
  "de": {
    "positive": {
      "default": {
        "standard": "{name} muss positiv sein"
      },
      "negative": {
        "standard": "{name} darf nicht positiv sein"
      }
    }
  },
  "custom": {
    "positive": {
      "default": {
        "standard": "Is this {name} positive? I don't think so..."
      },
      "negative": {
        "standard": "{name} must NOT be positive"
      }
    }
  }
}
```

In example above we defined 3 languages (_en_, _de_ and _custom_). Every language has messages for only 
one rule - _positive_.

There are two ways to select language from multi-language:

- set default language for provided translation
- set language for rule chain

### Example

```python
from respect_validation import Validator as v, Factory
from respect_validation.Exceptions import NestedValidationException

# our translation dictionary with several languages
translation = {
  "en": {
    "positive": {
      "default": {
        "standard": "{name} must be positive"
      },
      "negative": {
        "standard": "{name} must not be positive"
      }
    }
  },
  "de": {
    "positive": {
      "default": {
        "standard": "{name} muss positiv sein"
      },
      "negative": {
        "standard": "{name} darf nicht positiv sein"
      }
    }
  },
  "custom": {
    "positive": {
      "default": {
        "standard": "Is this {name} positive? I don't think so..."
      },
      "negative": {
        "standard": "{name} must NOT be positive"
      }
    }
  }
}

# set translation dict in the Factory and set default language
Factory.set_translation(translation).default_language('de')
# also you can separate this like so:
# Factory.set_translation(translation)
# Factory.default_language('de')
# doesn't matter :)

# we translated only positive rule, then numericVal will have default messages
try:
    v.numericVal().positive().claim('ggg')
except NestedValidationException as nve:
    print(nve.get_messages())
    print(nve.get_full_message())

# another example, where we set language
try:
    v.numericVal().positive().set_language('custom').claim('ggg')
except NestedValidationException as nve:
    print(nve.get_messages())
    print(nve.get_full_message())
```
Output:
```text
# the first try
# nve.get_messages()
{'numericVal': ['"ggg" must be numeric'], 'positive': ['"ggg" muss positiv sein']}
# nve.get_full_message()
- All of the required rules must pass for "ggg"
  - "ggg" must be numeric
  - "ggg" muss positiv sein

# the second try
# nve.get_messages()
{'numericVal': ['"ggg" must be numeric'], 'positive': ['Is this "ggg" positive? I don\'t think so...']}
# nve.get_full_message()
- All of the required rules must pass for "ggg"
  - "ggg" must be numeric
  - Is this "ggg" positive? I don't think so...
```

!!! info
    If you want to use multi-language but don't set default language in Factory (`.default_language(...)`), 
    then default messages will appear until you will add `.set_language(...)` method for rule chain.