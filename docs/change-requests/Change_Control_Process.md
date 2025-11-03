# Change Control Process

**Project:** Calculator Application  
**Prepared by:** Muhtasim Sani  
**Date:** 2025-11-03  

---

## 1. Purpose
This document defines the procedure for requesting, reviewing, approving, or rejecting changes to the Calculator Application.

---

## 2. Change Request Workflow

| Step | Action | Responsible Person | Output |
|------|---------|--------------------|---------|
| 1 | **Submit Change Request (CR):** Any team member identifies a need for change and completes a CR form. | Requester | Change Request Form (CR-###) |
| 2 | **Review:** The team lead reviews the request for clarity and feasibility. | Reviewer | Comments / Request for Clarification |
| 3 | **Impact Analysis:** The developer assesses how the change affects code, cost, time, and quality. | Developer | Impact Assessment |
| 4 | **Decision:** Team approves or rejects based on impact. | Project Lead / Team | Approval or Rejection note |
| 5 | **Implementation:** If approved, change is made and committed to a new branch. | Developer | Code Update, Commit Message |
| 6 | **Verification:** QA/tests confirm that the change works. | Tester | Test Report |
| 7 | **Closure:** CR is marked *Closed* after verification. | Project Lead | Updated CIL and SCM Report |

---

## 3. Change Identification
Each CR will have a unique ID (e.g., **CR-001**, **CR-002**) and will be stored under:  
`docs/change-requests/`

---

## 4. Tools Used
- GitHub Issues / Pull Requests (for discussion and approvals)  
- Markdown CR forms in `docs/change-requests/`  
- Git commit messages referencing CR IDs (e.g., `fix: handle division by zero [CR-001]`)

---

## 5. Approval Authority
| Role | Name | Responsibility |
|------|------|----------------|
| Project Lead | Muhtasim Sani | Approve / reject changes |
| Developer | Team Member A | Implement approved changes |
| Reviewer | Team Member B | Review proposed changes |

---
