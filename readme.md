# pseudo

A console application that helps you run [SudoLang](https://github.com/paralleldrive/sudolang-llm-support) programs easily using the OpenAI API.

## Pre-requisites
Set your `OPENAI_API_KEY` environment variable.

## Installation
To install pseudo, run the following command:

```shell
chmod +x install.sh
./install.sh
```
## Usage

To use pseudo, execute the following command:

```shell
pseudo programs/code-reviewer.sudo
```
This repository includes a submodule to the official repository [SudoLang](https://github.com/paralleldrive/sudolang-llm-support), which has a wide number of examples to choose from.

Exampe:

```shell
pseudo sudolang-llm-support/examples/ai-rpg.sudo.md
```
