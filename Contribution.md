# 🤝 Contributing to Pakistan Crop Price Analysis

Thank you for your interest in contributing to this project! This document outlines the guidelines and workflow for contributing effectively — whether you are a team member or an external collaborator.

---

## 📚 Table of Contents

- [Project Team](#-project-team)
- [Code of Conduct](#-code-of-conduct)
- [How to Get Started](#-how-to-get-started)
- [Branch Strategy](#-branch-strategy)
- [Making Changes](#-making-changes)
- [Commit Message Guidelines](#-commit-message-guidelines)
- [Pull Request Process](#-pull-request-process)
- [Notebook Contribution Guidelines](#-notebook-contribution-guidelines)
- [Reporting Issues](#-reporting-issues)
- [Style Guide](#-style-guide)


## 🧭 Code of Conduct

All contributors are expected to:

- Be respectful and constructive in all communications.
- Give credit where it is due — always reference sources and dataset authors.
- Keep discussions focused on the project.
- Review each other's work honestly and professionally.
- Not push directly to `main` without a reviewed pull request.

---

## 🚀 How to Get Started

### 1. Fork or Clone the Repository

If you are a **team member**, clone directly:
```bash
git clone https://github.com/<your-username>/pakistan-crop-price-analysis.git
cd pakistan-crop-price-analysis
```

If you are an **external contributor**, fork first:
1. Click **Fork** on the top-right of the repository page.
2. Clone your fork:
```bash
git clone https://github.com/<your-fork>/pakistan-crop-price-analysis.git
```

### 2. Set Up Your Environment

```bash
# Install required Python packages
pip install pandas numpy matplotlib seaborn statsmodels scikit-learn jupyter
```

Or if a `requirements.txt` is available:
```bash
pip install -r requirements.txt
```

### 3. Download the Dataset

The raw dataset is not included in this repository due to its size (~7.99M records). Download it from Kaggle and place it in the `pakistan_crop_prices_dataset/` folder:

📎 https://www.kaggle.com/datasets/humairarana/crop-prices-dataset-of-pakistan

---

## 🌿 Branch Strategy

We follow a simple feature-branch workflow:

```
main
 └── deliverable-1        ← Completed
 └── deliverable-2        ← Active development
 └── feature/<name>       ← Individual feature work
 └── fix/<name>           ← Bug fixes
```

| Branch Type | Naming Convention | Example |
|-------------|------------------|---------|
| Feature | `feature/<short-description>` | `feature/arima-modeling` |
| Bug Fix | `fix/<short-description>` | `fix/outlier-removal-bug` |
| Deliverable | `deliverable-<number>` | `deliverable-2` |
| Experiment | `experiment/<short-description>` | `experiment/lstm-trial` |

### Creating a New Branch

```bash
# Always branch off from main
git checkout main
git pull origin main
git checkout -b feature/your-feature-name
```

---

## ✏️ Making Changes

1. Make your changes in the appropriate notebook section or script.
2. Save all notebook outputs before committing (run all cells first).
3. Place any new output charts in the correct subfolder under `outputs/`.
4. Update the `README.md` if your changes affect the pipeline, milestones, or outputs.

---

## 💬 Commit Message Guidelines

We follow a simple and consistent commit message format:

```
<type>: <short description>
```

### Types

| Type | When to Use |
|------|------------|
| `feat` | Adding a new feature or analysis stage |
| `fix` | Fixing a bug or incorrect output |
| `data` | Changes related to data loading or preprocessing |
| `viz` | Adding or updating visualizations |
| `docs` | Updating README, CONTRIBUTING, or report files |
| `refactor` | Restructuring code without changing behavior |
| `chore` | Dependency updates, file cleanup, config changes |

### Examples

```bash
git commit -m "feat: add ARIMA model training for top 5 crops"
git commit -m "fix: correct IQR outlier removal groupby logic"
git commit -m "viz: add seasonal decomposition charts for Garlic and Banana"
git commit -m "docs: update milestones table in README for Deliverable 2"
git commit -m "data: handle zero-price entries before normalization"
```

---

## 🔁 Pull Request Process

1. Push your branch to GitHub:
```bash
git push origin feature/your-feature-name
```

2. Open a **Pull Request** from your branch into `main`.

3. Fill in the PR description with:
   - What you changed and why
   - Which milestone or deliverable this relates to
   - Any known issues or open questions

4. Request a review from at least **one other team member**.

5. Address any review comments before merging.

6. Once approved, the author or reviewer merges into `main`.

> ⚠️ **Never force-push to `main`.** Always merge via PR.

---

## 📓 Notebook Contribution Guidelines

Since the main deliverable is a Jupyter Notebook, follow these rules:

- **Run all cells before committing** — never commit a notebook with stale or missing outputs.
- **Keep sections modular** — each pipeline stage (`01_`, `02_`, etc.) should be self-contained and runnable independently.
- **Add markdown cells** to explain each function and pipeline stage clearly.
- **Do not hardcode paths** — use relative paths or configurable variables at the top of the notebook.
- **Save output charts** to the correct `outputs/` subfolder using the `save_and_show()` helper function.
- **Avoid print-heavy cells** — keep console output clean and informative.

---

## 🐛 Reporting Issues

If you find a bug, incorrect output, or want to suggest an improvement:

1. Go to the **Issues** tab on the GitHub repository.
2. Click **New Issue**.
3. Choose the appropriate label:
   - `bug` — something is broken or producing wrong results
   - `enhancement` — a suggestion for improvement
   - `question` — clarification needed
   - `documentation` — README or report issue
4. Provide as much detail as possible — include the cell number, error message, or chart name.

---

## 🎨 Style Guide

### Python
- Follow **PEP 8** formatting conventions.
- Use descriptive function and variable names.
- Add a docstring to every function explaining its purpose, inputs, and outputs.
- Group imports at the top: standard library → third-party → local.

### Visualizations
- Always set a `title`, `xlabel`, and `ylabel` on every plot.
- Use `bbox_inches="tight"` when saving figures.
- Save all figures to the correct `outputs/` subfolder — never leave plots only in notebook memory.
- Use consistent color schemes across related charts.

### File Naming
- Output charts: `snake_case.png` (e.g., `moving_average_advanced.png`)
- Notebooks: `DM_Project_Deliverable_<N>.ipynb`
- Reports: `DM_<ReportName>.docx`

---

## 📄 License

By contributing to this project, you agree that your contributions will be licensed under the same [MIT License](./LICENSE) that covers the project.

---

<div align="center">

*FAST-NUCES · Data Mining · Spring 2026*

</div>
