# Training Repository

This repository contains LLM training experiments and utilities for reasoning and planning.

## Project Structure

```
training/
├── src/training/           # Main package source code
│   ├── __init__.py        # Package initialization
│   ├── agent_prompts.py   # Agent prompting utilities
│   ├── format_verifier.py # Format verification functions
│   ├── hello.py           # Hello world example
│   ├── planner_schema.py  # Planning schema definitions
│   └── reasoning_schema.py # Reasoning schema definitions
├── notebooks/             # Jupyter notebooks for analysis
│   ├── dataset_analysis.ipynb
│   └── testing_attention.ipynb
├── tests/                 # Test files (empty for now)
├── pyproject.toml        # Project configuration
├── uv.lock              # UV lock file
└── README.md            # This file
```

## Setup

This project uses UV for dependency management. Make sure you have UV installed and the environment is activated.

## Usage

Import the training package:

```python
from src.training import format_verifier, reasoning_schema, planner_schema
```
