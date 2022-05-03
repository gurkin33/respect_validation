# Extension

- `Extension(extension: str)`

Validates if the file extension matches the expected one:

```python
v.extension('png').validate('image.png')  # true
```

This rule is case-sensitive.

## Categorization

- File system

## Changelog

Version | Description
--------|-------------
  1.0.0 | Created

***
See also:

- [Directory](Directory.md)
- [Executable](Executable.md)
- [Exists](Exists.md)
- [File](File.md)
- [Image](Image.md)
- [Mimetype](Mimetype.md)
- [Readable](Readable.md)
- [Size](Size.md)
- [SymbolicLink](SymbolicLink.md)
- [Writable](Writable.md)