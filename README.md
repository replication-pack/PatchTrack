# PatchTrack

## Introduction
`PatchTrack`: Enhancing Software Patch Decision-Making in Pull Requests Using ChatGPT. This tool relies on clone detection to mine cases of missed opportunity and effort duplication from a pool of patches.

## Directory Structure
```
.
├── LICENSE
├── README.md
├── docs
├── mkdocs.yml
├── requirements.txt
├── tokens-example.txt
├── PatchTrack.py
├── src
│   ├── bin
│   ├── constants
│   ├── core
│   ├── utils
│   ├── legacy
│   ├── notebooks
│   └── tests
└── 
```

## Setting up 
To setup and test `PatchTrack` tool on your local computer, following the steps below:
### Get the code
The easiest way is using the `git clone` command:

```bash
git clone https://github.com/replication-pack/PatchTrack.git
```
### Dependencies
`PatchTrack` consist of two categories of depencies i.e. (i) OS specific dependencies and (ii) development dependencies. The OS specific dependency is `libmagic`. To install this dependency on `Ubuntu/Debian` or `MacOS X`, run the shell script in the `bin` directory.

```bash
cd bin/
chmod +x script.sh
./script.sh
```
The above code will automatically detect the OS (Linux or MacOS X) and install the libraries.
Before installing development specific dependencies, let's set python virtual environment;

```bash
cd PatchTrack/

python3 -m venv venv
```
Activate the virtual environment 

```bash
source venv/bin/activate
```

Now, let us install the dependencies

```bash
pip install -r requirements.txt
```
Note: `PatchTrack` has been tested on `python >= 3.7`


