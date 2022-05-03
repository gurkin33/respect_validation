# Image

- `Image()`

Validates if the file is a valid image by checking its MIME type.

```python
v.image().validate('image.gif')  # true
v.image().validate('image.jpg')  # true
v.image().validate('image.png')  # true
```

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
- [Extension](Extension.md)
- [File](File.md)
- [Mimetype](Mimetype.md)
- [Readable](Readable.md)
- [Size](Size.md)
- [SymbolicLink](SymbolicLink.md)
- [Writable](Writable.md)