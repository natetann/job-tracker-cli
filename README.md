# Job Tracker CLI v0.1.0

## Description
A command-line interface (CLI) tool for tracking job applications. It allows users to add, view, update, and delete job applications. The tool does this in a visually appealing way using the `rich` library for formatting and `InquirerPy` for interactive prompts. Storage is handled locally by `SQLite3`.

## Features
- Add new job applications with details such as title, company, location, type, and status.
- View all job applications in a formatted table.
- Update existing job applications by ID and specific fields.
- Delete job applications by ID.
- (Planned) Generate a Sankey graph to visualize job application statuses. 

## Requirements
- `Python 3.10` or higher, although it may work with earlier versions.
- (Planned) `pip` for installing dependencies.

## Installation
### (Planned) Through pip:
```bash
pip install job-tracker-cli
```
### From source:
1. Clone the repository:
```bash
git clone https://github.com/natetann/job-tracker-cli.git
```
2. Navigate to the project directory:
```bash
cd job-tracker-cli
```
3. OPTIONAL (recommended): Create a virtual environment:
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On macOS/Linux
```
4. Install the package:
```bash
pip install .
```

## Usage
After installation, you can run the CLI tool using the following command:
```bash
jobcli
```