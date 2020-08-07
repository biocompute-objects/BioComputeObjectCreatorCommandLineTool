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

This tool's dependencies include the `jsons` package in python which can be installed with `python3 -m pip install jsons` 

Download this tool's code from github in same directory where you intend to use it or use the following command:

```
wget https://raw.githubusercontent.com/p-m-ishra/BioComputeObjectCreatorCommandLineTool/master/biocompute_command_line_tool.py
```

If you would like to clone this repository: 

```
git clone https://github.com/p-m-ishra/BioComputeObjectCreatorCommandLineTool.git
```

## Usage

* Current Prerequisites
  * Pipeline must be on first line of input after script started message (E.g. after this line: `Script started on 2020-08-01 15:21:02-0400`) 
  * Pipeline must be one line long
  * Symbol after working directory must be $ or # (E.g. `pranav@laptop:~$` or `root@laptop:~#`)

Place `biocompute_command_line_tool.py` in the same directory as the output of the `script` command that recorded the computational workflow or analysis pipeline.

Then run the following command:
```
python3 biocompute_command_line_tool.py 
```

Navigate to [BioCompute Portal](https://portal.aws.biochemistry.gwu.edu/bco/new/form#!)

Click `edit json` and paste the output from the json file.

Finally, click `submit` to create your BioCompute Object.

For a walkthrough of the command line portion of this tool, click [here](https://drive.google.com/file/d/1ivy-4i-TMmwSJQKQf0d_aY0NuiPQF50S/view?usp=sharing).

## API

## Documentation

**Classes and Objects**
For each domain, there is a class with all required and optional fields in that domain. Additionally, some subdomains have their own classes as they have their own specific fields. Items in an array also have their own class if they have multiple fields (E.g. parameter object fills the parametric domain array) Optional fields are set to NoneType if the user opts not to enter them. Currently, the user is not prompted to enter optional fields. The remove_nulls method insures that NoneType fields are not included in the output json file.

**Automatic Pipeline Breakdown**
To read in the output script file, the first line (E.g. `Script started on 2020-08-01 15:21:02-0400`) is cut from the input text and the pipeline is defined as the first occurence of a $ or # to the next occurence of a newline (\n) character. 

In the following example from the [example input file](https://github.com/p-m-ishra/BioComputeObjectCreatorCommandLineTool/blob/master/biocompute_input.txt), the first line would be cut and then ` cat input.txt | grep "ham" | sed -n '/ham?$/p' > output.txt` would be the pipeline.

```
Script started on 2020-08-01 15:21:02-0400
pranav@LAPTOP-CHO8EET5:/mnt/c/Users/pranav/Documents/GWU/BioCompute$ cat input.txt | grep "ham" | sed -n '/ham?$/p' > output.txt
```
For the description domain, pipeline steps are identified by splitting by the '|' character. Each step is now part of a list. Then, each individual step is split by the ' ' character and the first item of the resulting list is registered as the tool. Users are able to confirm and edit the tool name in case the automatic prediction is incorrect.

For the parametric domain, pipeline steps are identified the same way. Then, a non-default parameter is identified through the presence of a " -" expression in the step. If that expression is present, the tool name is identified by splitting by the ' ' character and taking the first item in the resulting list. The non-default parameter value is identified by taking the remaining string, finding the index of the " -" expression and then cutting the aforementioned remaining string into the index of that expression to the next occurence of a ' '  character. Users are given an option to delete and edit automatically identified parameters. They are also able to add parameters that were not automatically identified.

**User Input** 
When user enters input separated by spaces, it is either broken into a list or put into a dictionary as a key:value pair. Most input that needs to be in a certain format has a try except block in order to make sure user can retry if they do not enter it in the correct format the first time. For fields that are not self-explanatory, the users receive a description describing what they should put into that field through a print statement. For fields that are not free text fields, the user receives directions on how to enter their input through a print statement.

While loops are used when users can add multiple inputs into a field that takes an array. The user is prompted after each input whether they would like to add another item. 

**File Saving**
First, the output file is saved without the etag, object_id, and spec_version fields. Then based on prior user input, it is hashed with MD5, SHA1, or SHA256. Then, the json file is resaved with the object_id, spec_version, and newly autogenerated etag. All intermediate (When file is saved without metadata fields) and final (final output file) file saving occurs in try except blocks and alerts user if there is an error saving the file.


## Issues

* Prompt user if they would like to change anything at the end
* Check formatting for email strings
* Get information from ORCID and API

## Contributing

See [the contributing file](CONTRIBUTING.md)!

PRs accepted.

## License

[MIT © Pranav Mishra](LICENSE)
