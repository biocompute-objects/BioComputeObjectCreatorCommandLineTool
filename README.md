# BioCompute Object Creator 

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This is a tool to create a BioCompute Object directly from the command line.

This tool creates an IEEE compliant [IEEE-2791 object](https://opensource.ieee.org/2791-object/ieee-2791-schema/).

## Table of Contents

- [Background](#background)
- [Install](#install)
- [Usage](#usage)
- [API](#api)
- [Contributing](#contributing)
- [License](#license)
- [Issues](#issues)

## Background

BioCompute is a standardized way to communicate an analysis pipeline. BioCompute substantially improves the clarity and reproducibility of an analysis, and can be packaged with other standards, such as the Common Workflow Language. An analysis that is reported in a way that conforms to the BioCompute specification is called a BioCompute Object (BCO). A BCO provides the structure that dictates what information must be present in a report. 

Additional BioCompute resources can be found [here](https://biocomputeobject.org/)

## Install

This module's dependencies include the `jsons` package in python which can be installed with `python3 -m pip install jsons` 

```
```

## Usage

Place `biocompute_command_line_tool.py` in the same directory as the output of the `script` command that recorded the computational workflow or analysis pipeline.

Then run the following command:
```
python 3 biocompute_command_line_tool.py 
```

## API

## Issues

- Prompt user if they would like to change anything at the end
- User specified etag (e.g. MD5, SHA-256)
- Output to json file in valid BCO format
- Check formatting for email strings

## Contributing

See [the contributing file](CONTRIBUTING.md)!

PRs accepted.

## License

[MIT © Pranav Mishra](LICENSE)
