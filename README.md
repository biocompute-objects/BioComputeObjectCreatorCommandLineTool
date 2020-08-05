# BioCompute Object Creator 

[![license](https://github.com/p-m-ishra/BioCompute-Object-Creator-Command-Line-Tool-/blob/master/LICENSE)](LICENSE)
[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

This is a tool to create a BioCompute Object directly from the command line.

This tool creates an IEEE compliant [IEEE-2791 object](https://opensource.ieee.org/2791-object/ieee-2791-schema/).

## Table of Contents

- [Background](#background)
- [Install](#install)
- [Usage](#usage)
- [API](#api)
- [Contributing](#contributing)
- [License](#license)

## Background

BioCompute is a standardized way to communicate an analysis pipeline. BioCompute substantially improves the clarity and reproducibility of an analysis, and can be packaged with other standards, such as the Common Workflow Language. An analysis that is reported in a way that conforms to the BioCompute specification is called a BioCompute Object (BCO). A BCO provides the structure that dictates what information must be present in a report. 

Additional BioCompute resources can be found [here](https://biocomputeobject.org/)

## Install

This module's dependencies include the 'jsons' package in python which can be installed with 'python3 -m pip install jsons' 

```
```

## Usage

Place 'biocompute_command_line_tool.py' in the same directory as the output of the 'script' command that recorded the computational workflow or analysis pipeline.

Then run the following command:
```
python 3 biocompute_command_line_tool.py 
```

Note: The `license` badge image link at the top of this file should be updated with the correct `:user` and `:repo`.

## API

## Contributing

See [the contributing file](CONTRIBUTING.md)!

PRs accepted.

Small note: If editing the Readme, please conform to the [standard-readme](https://github.com/RichardLitt/standard-readme) specification.

## License

[MIT © Pranav Mishra](LICENSE)
