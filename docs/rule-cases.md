# Rule "cases" (spelling)

All rule names support two type of cases (spelling):

- CamelCase
- `snake_case` ([PEP8][pep8])

## CamelCase

It is the same name as rule's class name. For example:

- StringType
- IntVal
- VideoUrl

!!! tip
    Also you can start rule name with the first lower letter - stringType, intVal. 
    It also works.

## snake_case

Based on PEP8 all methods [must have `snake_case` names][pep8-method], then you can add all rules 
in this shape. For example:

- string_type
- int_val
- video_url

!!! attention
    Your custom rules must not have _ (underscores) in names, else you get error. 
    Based on PEP8 all class names must be in [CamelCase (CapWords)][pep8-class].

[pep8]: https://legacy.python.org/dev/peps/pep-0008/
[pep8-class]: https://legacy.python.org/dev/peps/pep-0008/#class-names
[pep8-method]: https://legacy.python.org/dev/peps/pep-0008/#method-names-and-instance-variables