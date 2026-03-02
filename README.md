[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/rZxQuJoV)
# AI.SPIRE Pre-Work — Python Toolchain

This repository is your workspace for Pre-Work Days 3–5.

| Day | PR | Topic |
|-----|-----|-------|
| 3 | PR-2 | Python venv Bootstrap + Sanity Script |
| 4 | PR-3 | Notebook vs Script: Same Output Two Ways |
| 5 | PR-4 | Compute & Debug Evidence Pack |

## Setup

Install Python 3.11 from [python.org](https://python.org), then:

```bash
python -m venv .venv
source .venv/bin/activate        # macOS / Linux
# source .venv/Scripts/activate  # Windows (Git Bash)
python -m pip install --upgrade pip
python -m pip install -r requirements-prework.txt

```
## About

[One paragraph: who you are and what this repository is for.]

## Setup

```bash
git clone https://github.com/LevelUp-Applied-AI/<your-username>-prework.git
cd <your-username>-prework

## Submitting PRs

1. Create a branch named for the PR task (e.g., `pr-02-python-env`)
2. Complete the work
3. Push the branch and open a PR from your branch to `main`
4. Submit the PR URL in TalentLMS
## When to use each

I would use a Jupyter notebook when I am exploring data, testing ideas, or analyzing results step by step. It is very helpful for interactive work because I can run cells one by one and immediately see the output.

I would use a Python script when I need to run code from the command line or make it part of a project. Scripts are better for automation, reproducibility, and running the same process multiple times.