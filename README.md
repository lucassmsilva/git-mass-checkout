#### Install dependencies
```
pip install gitpython
```

#### Add depencies in the key:value format on repositories.py
###### Example:

```
REPOS = {
    'dependency-injection': 'https://github.com/lucassmsilva/dependence-injection.git',
    'reactivity': 'https://github.com/lucassmsilva/vue-3-reactivity.git',
    # Add more repositories as needed
}
```

#### Use
```
python checkout.py
```