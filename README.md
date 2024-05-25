# PatchTrack: Enhancing Software Patch Decision-Making in Pull Requests Using ChatGPT

## Introduction
`PatchTrack`: Enhancing Software Patch Decision-Making in Pull Requests Using ChatGPT. This tool relies on clone detection to determine whether patches were applied, not applied, or not suggested by ChatGPT during ChatGPT-Developer conversation.

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
### Minimum System Requirements
- `Operating System`: Mac0SX, Linux, Windows
- `RAM`: >= 4 GB
- `Storage`: >= 1 GB
- `Processor`: CPU 1.18 GHz or greater
#### Other tools
- Git, Python >= 3.11
### Python Virtual Environment
let's set python virtual environment;

```bash
cd PatchTrack/

python3 -m venv venv
```
Activate the virtual environment 

```bash
source venv/bin/activate
```
### Dependencies and Dataset

`PatchTrack` consist of two categories of depencies i.e. (i) OS specific dependencies and (ii) development dependencies. The OS specific dependency is `libmagic`. To dependencis will be installed automatically when you start the tool. You can also install manually on `Ubuntu/Debian` or `MacOS X`, by runing the shell script in the `bin` directory.

```bash
cd bin/
chmod +x os-package.sh
./os-package.sh
```
The above code will automatically detect the OS (Linux or MacOS X) and install the libraries.
Before installing development specific dependencies.

Datasets are stored in the `dataprep` directory in zipped files. This will be automatically extracted and placed in the right directory using the step below. Now, let us install the dependencies and load the required datasets.

```bash
python PatchTrack.py --init
```
The above command will install all the required packages, set directories and unzip datasets for the smooth execution of the tool.
Note: `PatchTrack` has been tested on `python >= 3.11`

## Running the tool
### Notebooks
This is the easiest approach to test the tool. In the `notebooks` directory, simply run the `run_experiment.ipynb` file. 
### Console

### List of Commands
Information of the other command line options are provided by using `-h` or `--help`
```
usage: PatchTrack.py [-h] [-i] [-n NUM] [-c NUM] [-v] [-p STR] [-s SOURCE_PATH] [-r]

options:
  -h, --help            show this help message and exit
  -i, --init            setup required datasets and directories. This command should be executed at least once
  -n NUM, --ngram NUM   use n-gram of NUM lines (default: 1)
  -c NUM, --context NUM
                        print NUM lines of context (default: 10)
  -v, --verbose         enable verbose mode (default: False)
  -p STR, --patch_path STR
                        path to ChatGPT and PR patch files (default: data/patches)
  -s SOURCE_PATH, --source_path SOURCE_PATH
                        path to json files of extracted ChatGPT conversations and code snippets (default: data/extracted)
  -r, --restore         restore default setting, files and directories
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
