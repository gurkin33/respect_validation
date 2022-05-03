# Call

- `Call(callable_fun: Any, rule: AbstractRule)`

Validates the return of a _callable_ for a given input.

Consider the following variable:

```python
url = 'https://www.google.com/search?q=respect.github.com'
```

To validate every part of this URL we could use `urlparse`
function to break its parts:

```python
from urllib.parse import urlparse
parts = urlparse(url)
```

This function returns an object ParseResult containing `scheme`, `netloc`, `path` and `query`.
We can validate them this way:

```python
v.attribute('scheme', v.startsWith('http'))\
    .attribute('netloc', v.domain())\
    .attribute('path', v.stringType())\
    .attribute('query', v.notEmpty())\
    .validate(parts)
```

Using `v.call()` you can do this in a single chain:

```python
v.call(
    urlparse,
    v.attribute('scheme', v.startsWith('http'))\
        .attribute('host',   v.domain())\
        .attribute('path',   v.stringType())\
        .attribute('query',  v.notEmpty())\
).validate(url)
```

## Categorization

- Callables
- Nesting

## Changelog

Version | Description
--------|-------------
  1.0.0 | Created

***
See also:

- [Callback](Callback.md)
- [Each](Each.md)