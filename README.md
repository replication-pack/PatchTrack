# PatchTrack: Enhancing Software Patch Decision-Making in Pull Requests Using ChatGPT

The utilization of Large Language Models (LLMs) in software development has increased significantly in recent years. However, understanding how conversational LLMs like ChatGPT can enhance collaborative software development remains limited, particularly in managing and integrating patches in pull requests. This study aims to address this gap by analyzing developers' shared ChatGPT conversations within merged GitHub pull requests. We curated a dataset comprising 464 ChatGPT-generated code snippets and 1,360 pull request patches from 183 pull requests. We then developed a tool, `PatchTrack`, to detect whether patches were applied, not applied, or not suggested by ChatGPT.

## Directory Structure and Description
```
.
├── LICENSE                     # The License for the tool - MIT License
├── PatchTrack.py               # Main entrypoint of the tool
├── README.md                   # Readme file to describe how the tool work
├── RQ1_2_3                     # Contains all the results for RQ1, RQ2 and RQ3
├── analyzer                    # Directory for core modules of the tool   
│   ├── __init__.py
│   ├── analysis.py             # Plotting the classification result
│   ├── classifier.py           # Classifies the dataset as PA, PN or NE
│   ├── common.py               # Setting n-grams, file types, etc
│   ├── constant.py             # All the constant variables used in the tool   
│   ├── dataDict.py             # Keep track of extracted pr-project-pair information 
│   ├── helpers.py              # All helper functions e.g. api requests, normalization, etc.
│   ├── main.py                 # Main PatchTrack class
│   ├── patchLoader.py          # Parse and tokenize PR patches. The file should be a diff format
│   ├── sourceLoader.py         # Parse and tokenize ChatGPT code snippet
│   └── totals.py               # Compute total number of PA, PN or NE classified
├── bin                         
│   └── os-packages.sh          # OS-specific dependencies 
├── dataprep                    
│   ├── __init__.py
│   ├── allPullRequestSharings.zip    # DevGPT and Extended json dataset   
│   ├── load.py                       # Functions for loading datasets
│   ├── manual                        # Procedures on how to generate the extended dataset
│   └── patches.zip                   # Extracted ChatGPT code snippest and PR patches
├── notebooks                    # Notebooks containing code for running the experiments
│   ├── __init__.py
│   └── run_experiment.ipynb
├── output                       # figures and csv files of all the results of running the tool
├── requirements.txt             # List of python dependencies required by the tool
├── tests                        # Testing different component of the tool. This is still a WIP
└── tokens-example.txt           # Example token file. This should be renamed to `tokens.txt`
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
