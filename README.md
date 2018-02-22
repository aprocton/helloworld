# helloworld

### Installation

Clone the repo and use pip to install it.

```bash
git clone https://github.com/aprocton/helloworld.git
cd helloworld/
pip install .
```

### CLI Usage

To use helloworld from the command line:

```bash
$ helloworld -h
usage: helloworld [-h] [-n NAME] [-d]

optional arguments:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  optional name to say hello to
  -d, --date            print today's date
```

### API Usage

To use the helloworld Python API:

```python
import helloworld
helloworld.helloworld(name="Alex", date=True)
```
