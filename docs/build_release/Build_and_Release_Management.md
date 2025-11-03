# Build and Release Management

**Project:** Calculator Application  
**Version:** v1.0  
**Prepared by:** Muhtasim Sani  
**Date:** 2025-11-03  

---

## 1. Purpose
This document defines how the Calculator Application is built, packaged, versioned, and released to end users. It ensures consistent and repeatable deployment.

---

## 2. Build Process

| Step | Description | Tool |
|------|--------------|------|
| 1 | Source code is stored and version-controlled in GitHub. | Git |
| 2 | Developer clones repository to local machine. | `git clone` |
| 3 | Code is verified for syntax and logic errors. | Python (VS Code terminal) |
| 4 | The program is executed and tested. | Python Interpreter |
| 5 | If all tests pass, the code is packaged as a release build. | Git/GitHub |

---

### Example Build Command
```bash
python src/calculator.py
