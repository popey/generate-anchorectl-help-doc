# Generate AnchoreCTL Help Doc

A Python script to generate comprehensive markdown documentation from the `anchorectl --help` command output.

## Introduction

This tool was created in response to a need in the Anchore community for accessible documentation of the `anchorectl` command line interface. While the CLI tool provides excellent help output, accessing this information requires installing and running the tool locally, which isn't always possible in restricted environments.

The script recursively traverses through all `anchorectl` commands and subcommands, capturing their help text and organizing it into a clean markdown document. This makes the CLI reference material easily accessible online, perfect for environments where installing the tool locally isn't practical.

## Installation

The script is written in Python and has minimal dependencies, primarily using standard library modules.

### Pre-requisites

The script requires:
- Python 3.x
- `anchorectl` binary in your PATH (only needed when generating documentation)

### Getting Started

```shell
git clone https://github.com/popey/generate-anchorectl-help-doc
cd generate-anchorectl-help-doc
./generate_anchorectl_help_doc.py
```

By default, the script looks for `anchorectl` in your PATH. You can specify a different path to the binary:

```shell
./generate_anchorectl_help_doc.py /path/to/anchorectl
```

## Output

The script generates a markdown file named `anchorectl-<version>-help.md` containing:

- Version information
- Full command reference
- All subcommands and their help text
- Command-line options and flags

The generated documentation is organized hierarchically, making it easy to navigate and read online.

## Example Output Structure

~~~markdown
# AnchoreCTL Command Line Reference

Generated on: 2025-02-13 15:21:01

## Version Information

```
Application:        anchorectl
Version:            5.14.0
SyftVersion:        v1.19.0
BuildDate:          2025-01-29T18:49:44Z
GitCommit:          2ec6095c00c18dfe1a105b90da29864a7d9ac93d
GitDescription:     v5.14.0
Platform:           linux/amd64
GoVersion:          go1.23.5
Compiler:           gc
```


## anchorectl account

```text
Account related operations

Usage:
  anchorectl account [command]

Available Commands:
  add         Create a new account
  delete      Delete the specified account, only allowed if the account is in the disabled state
  disable     Disable an account
  enable      Enable a previously disabled account
  get         Get info about an account
  list        List account summaries
  update      Update an account

Flags:
  -h, --help   help for account

Use "anchorectl account [command] --help" for more information about a command.

For help regarding global flags, run --help on the root command
```
...
~~~

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests if you find bugs or have ideas for improvements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

Thanks to the Anchore community for inspiring this tool through their need for accessible CLI documentation.