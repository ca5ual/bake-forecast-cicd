# Bake Forecast CI/CD

## Overview

This repository contains a Python project that predicts the number of cookies to bake based on historical sales data. It also implements DevOps best practices including CI/CD, linting, type checking, security checks, testing, and package publishing.

## Features

- Predicts daily cookie bake quantities from CSV data.
- Built-in **logging** to track processing steps and potential issues.
- Fully typed Python code.
- Includes automated testing and validation.
- Implements CI/CD pipelines with GitHub Actions.
- Linting with `ruff` and formatting with `black`.
- Build automation for Python packages.
- Optional publishing to TestPyPI or PyPI on release.

## CI/CD

- The project includes GitHub Actions workflows to:
- Run tests on every push and pull request.
- Check code formatting, types, and security.
- Build Python distributions automatically.
- Optionally publish packages on release.

## Usage Example

Install the package from PyPI and try it with prepared .csv file in this repo:
```bash
pip install bake-forecast-cicd
get_average_bakes sold_items_1.csv

# Bake Forecast CLI

This tool processes a CSV file with sold items and provides a recommended number of cookies to bake today.

## Example Usage

```bash
get_average_bakes sold_items_1.csv -v
```

## Example Output (Verbose Mode)

```
[2025-11-30 15:17:29] DEBUG    bake_forecast.cli: Verbose logging enabled.
[2025-11-30 15:17:29] DEBUG    bake_forecast.cli: Received verbose flag: True
[2025-11-30 15:17:29] DEBUG    bake_forecast.cli: Received file path: sold_items_1.csv
[2025-11-30 15:17:29] INFO     bake_forecast.cli: Starting processing file 'sold_items_1.csv'
[2025-11-30 15:17:29] INFO     bake_forecast: Processed 21 rows.

--RESULT--
[2025-11-30 15:17:29] DEBUG    bake_forecast.cli: Process finished with success.
[2025-11-30 15:17:29] INFO     bake_forecast.cli: Recommended number of cookies to bake today is: **67.3**
```

## Example Output (Verbose Mode)

```
$ get_average_bakes nonexistent.csv -v
[2025-11-30 15:20:01] DEBUG    bake_forecast.cli: Verbose logging enabled.
[2025-11-30 15:20:01] WARNING  bake_forecast.cli: File not found error.
Double check file path.
```

## About the Calculation

The application calculates the average number of cookies sold based on the content of the provided CSV file and uses this value as the recommended amount to bake.

## Notes

* Use the `-v` flag to enable verbose logging.
