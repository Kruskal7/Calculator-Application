# Configuration Item List (CIL)

**Project:** Calculator Application  
**Prepared by:** Muhtasim Sani  
**Date:** 2025-11-03

---

## Purpose
This document identifies and lists all configuration items (CIs) for the Calculator Application.
Each CI is given a unique identifier (CI-###), a clear description, repository location, owner and version.

---

## Configuration Item List

| CI ID  | Item Name                          | Description                                                          | Type               | Location / Path                      | Owner                    | Version |
|:------:|------------------------------------|----------------------------------------------------------------------|--------------------|---------------------------------------|--------------------------|:-------:|
| CI-001 | calculator.py                      | Main application source code implementing arithmetic functions       | Source Code        | `src/`                                | Developer                | v1.0    |
| CI-002 | README.md                          | Project overview, setup and run instructions                         | Documentation      | `/`                                   | Project Lead             | v1.0    |
| CI-003 | .gitignore                         | Git ignore rules for local/IDE/system files                          | Config File        | `/`                                   | Version Control Specialist| v1.0    |
| CI-004 | CIL.md                             | This Configuration Item List document                                | Documentation      | `docs/`                               | Configuration Manager    | v1.0    |
| CI-005 | CR-001.md                          | Change Request 001 — Add modulus operation (Approved)                | Change Request     | `docs/change-requests/`               | Change Control Officer   | v1.0    |
| CI-006 | CR-002.md                          | Change Request 002 — Add GUI (Rejected)                              | Change Request     | `docs/change-requests/`               | Change Control Officer   | v1.0    |
| CI-007 | Build_and_Release_Management.md    | Build and release process description                                | Documentation      | `docs/build-release/`                 | Build Engineer           | v1.0    |
| CI-008 | CHANGELOG.md                       | Changelog listing released versions and notes                        | Documentation      | `docs/build-release/`                 | Configuration Manager    | v1.0    |
| CI-009 | Configuration_Audit_Report.md      | Results of the configuration audit and checklist                     | Documentation      | `docs/audit/`                         | QA / Tester              | v1.0    |
| CI-010 | Configuration_Status_Report.md     | Configuration Status Report (CSR) summarizing changes and issues     | Documentation      | `docs/audit/`                         | QA / Tester              | v1.0    |
| CI-011 | docs/change-requests/               | Folder containing all CR documents                                   | Documentation      | `docs/change-requests/`               | Change Control Officer   | v1.0    |
| CI-012 | docs/build-release/                 | Folder containing build & release docs and changelog                 | Documentation      | `docs/build-release/`                 | Build Engineer           | v1.0    |
| CI-013 | docs/audit/                         | Folder containing audit & CSR documents                              | Documentation      | `docs/audit/`                         | QA / Tester              | v1.0    |
| CI-014 | tests/                              | Folder reserved for test cases (unit/integration tests)              | Test Files         | `tests/`                              | QA / Tester              | v1.0    |
| CI-015 | scripts/build.sh (optional)         | Script to build/run the application (if present)                     | Script             | `scripts/`                            | Build Engineer           | v1.0    |

---

## Notes
- Any new CI added to the project must be recorded in this CIL with a new CI ID and committed to the repository.
- Version numbers will be updated as changes are approved and baselined (e.g., v1.1, v2.0).
- Use commit messages that reference CI IDs or CR IDs where applicable (e.g., `feat: add modulus [CR-001]`).

