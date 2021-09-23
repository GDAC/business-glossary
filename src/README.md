# GDAC Business Glossary

This repository contains the _GDAC Business Glossary_ work of the Government Data Architecture Community (GDAC) Business Glossary Sub-group.

- [Documentation](https://rossbowen.github.io/glossary/)

### Building the vocabulary

The vocabulary is available as a [turtle file](./terms.ttl) and is managed using the Office for National Statistics' [VocBench](http://vocbench.uniroma2.it/) instance.

### Building the documentation

The documentation makes use of github pages and is built from the vocabulary directly using a [python script](./process.py) and a [jinja2 template](./template.html).

Changes to the introduction section should be made to the repository's [README](../README.md) file. Changes to the HTML output should be made to the template [README](./template.html) file.

The styling is created using a [custom profile](./src/respec-profile) of [W3C's Respec](https://github.com/w3c/respec) library.

```sh
docker run --rm -v $PWD/..:/workspace -w /workspace -it python:latest \
/bin/bash -c "cd src; python -m pip install -r requirements.txt; python3 process.py"
```
