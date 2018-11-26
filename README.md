# PyCodeExec
Simple python library that can execute arbitrary code from supported programming languages via docker.
#### Requires a local Docker install

[![Build Status](https://jenkins.isogen.net/buildStatus/icon?job=pycodeexec)](https://jenkins.isogen.net/job/pycodeexec/)

# Usage

### Synchronous JavaScript 
```python
from pycodeexec import Runner

javascript = Runner("javascript")
output = javascript.get_output("console.log([...Array(10)].map(i=>i*i))")

print(output) 
# [ 0, 1, 4, 9, 16, 25, 36, 49, 64, 81 ]
```

### Also supports Asyncio
```python
from pycodeexec.asyncio import Runner

javascript = Runner("javascript")
await javascript.is_ready()
output = await javascript.get_output("console.log([...Array(10)].map(i=>i*i))")

print(output)
# [ 0, 1, 4, 9, 16, 25, 36, 49, 64, 81 ]

```

# Supported Languages
* Python
* JavaScript
* Ruby
* C
* More to come

# Installation
```bash
pip install pycodeexec
```

# TODO
* Execution limits
* List supported languages
* Come up with better names for everything
* Stream output via generator or something
* More supported languages

# Contributing
If anyone ever reads this, adding languages is really easy and that'd be an easy way to contribute.  Otherwise, submit a pull request.
