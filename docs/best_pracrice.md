# Best practice

Many of available rule can switch between types and compare data of different types. If you know what type 
do you expect, then better to set this check.

For example, we expect to get `int`, then we set `intType` check at the beginning of validation:
```python
v.intType().between(1, 100).validate(10)  # true
v.intType().between(1, 100).validate('10')  # false
```

If for some reason we want to have number in string type, there is no need to convert it to 
integer, just add addition validation:

```python
v.digit().between(1, 100).validate('10')  # true
```
Many of rules can switch type of variable for you, please visit [comparable values](./comparable-values.md) 
for more information.

!!! success
    **Best practice is to set validation as close as you can to your expectations for final data**
