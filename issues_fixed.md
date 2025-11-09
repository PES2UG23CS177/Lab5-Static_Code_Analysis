# Static Code Analysis – Issues Fixed

| Issue | Type | Tool | Line(s) | Description | Fix |
|--------|------|------|----------|--------------|------|
| Mutable default argument | Bug | Pylint | 11 | `logs=[]` reused between calls | Changed to `logs=None` and initialized inside function |
| Broad exception | Code Smell | Pylint | 28 | `except:` hides all errors | Replaced with specific exceptions and logging |
| Insecure use of eval() | Security | Bandit | 67 | `eval()` could execute arbitrary code | Removed or replaced with safe alternative |
| Unclosed files | Maintainability | Bandit/Pylint | 45, 55 | Files opened without context manager | Used `with open()` safely |
| Input type not validated | Runtime Bug | Manual | 13 | Crashed when invalid data passed | Added `isinstance()` checks |
| Old-style string formatting | Style | Flake8 | 16 | Used `%` instead of f-string | Replaced with f-strings |
