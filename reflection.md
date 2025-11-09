# Reflection – Lab 5: Static Code Analysis

### 1. Which issues were easiest or hardest to fix?
- **Easiest:** Formatting issues (unused imports, indentation, f-strings).
- **Hardest:** Mutable default arguments and input validation because they required logic changes.

### 2. Did the static analysis tools report any false positives?
- Yes, Pylint flagged some minor issues that didn’t actually cause problems (like unused variables in logging).

### 3. How would you integrate static analysis tools into a real development workflow?
- Integrate **Pylint**, **Bandit**, and **Flake8** into a **CI/CD pipeline** (e.g., GitHub Actions) so every push is automatically analyzed.
- Developers can also use **pre-commit hooks** to catch issues before commits.

### 4. What improvements were observed after applying fixes?
- Code became more secure, readable, and stable.
- It no longer crashes on invalid inputs.
- Logs and file handling are safer.
- The program now follows better Python coding standards.
