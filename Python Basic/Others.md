# Some Other Tips

For those which are uncategorized tips will be documented here. They will be in separated files once there is enough quantity of contents.



## Naming Rules

### Dummy Variables

If there is nothing special about(or just don't care about) a variable, we'll use `_` to represent it.

```python
#unpacking Tuple
city, _, population = ("Nantou", "Taiwan", 100000)
city, ignored, population = ("Nantou", "Taiwan", 100000) #equivalent

#extended unpacking Tuple
record = ("Taipei", "Taiwan", 4000000)
city, *_, population = record
city, *ignored, population = record #equivalent
```

