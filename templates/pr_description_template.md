# Pull Request Description Template

## Overview

[Briefly describe what this PR accomplishes in 1-3 sentences.
What problem does it solve?]

---

## Changes Summary

[What did you change and why? Link to related issues if applicable.]

```text
Fixes: #issue_number
Related to: #another_issue
```

---

## Review Checklist

### Clean Code ✅

- [ ] **Naming Conventions**
  - [ ] Variables, functions, and classes use descriptive names
  - [ ] No vague names like `x`, `temp`, `data` without context
  - [ ] Follows project naming conventions (snake_case, camelCase, etc.)

- [ ] **Code Structure**
  - [ ] Functions are single-purpose and small (< 50 lines preferred)
  - [ ] Logical grouping of related functionality
  - [ ] No duplicate code blocks

- [ ] **Readability**
  - [ ] Consistent indentation and formatting (black/isort/autopep8 applied)
  - [ ] Meaningful comments where non-obvious logic exists
  - [ ] No dead code, commented-out imports, or unused variables

- [ ] **Error Handling**
  - [ ] Appropriate exceptions raised/catched
  - [ ] Error messages are descriptive and actionable
  - [ ] Graceful degradation where applicable

### Unit Tests ✅

- [ ] **Test Coverage**
  - [ ] All new/modified code has corresponding tests
  - [ ] Edge cases covered (empty inputs, boundaries, exceptions)
  - [ ] Test coverage maintained above project threshold

- [ ] **Test Quality**
  - [ ] Tests are named descriptively (`test_function_name_when_condition_then_expected_result`)
  - [ ] Each test asserts a single behavior
  - [ ] No reliance on global state or external dependencies
  - [ ] Tests run in reasonable time (< 10s per file)

- [ ] **Test Organization**
  - [ ] Test files follow project structure conventions
  - [ ] Tests grouped logically (setup/teardown, test cases)
  - [ ] Mocking used appropriately for external services

### Documentation ✅

- [ ] **Inline Docs**
  - [ ] Docstrings added for public functions/classes
  - [ ] Parameters and return values documented
  - [ ] Examples provided where helpful

- [ ] **Commit Messages**
  - [ ] Follows conventional commits format
  - [ ] Describes what, not just how
  - [ ] References issues when applicable

- [ ] **External Docs**
  - [ ] README updated with new features/config options
  - [ ] API docs updated (if applicable)
  - [ ] CHANGELOG updated for user-facing changes

- [ ] **Comments**
  - [ ] Complex algorithms explained
  - [ ] Workarounds documented with context
  - [ ] No inline TODOs without action items

---

## Testing Performed

```text
- [x] Ran tests locally: pytest (or relevant test runner)
- [x] Tested new functionality manually
- [x] Verified no regressions in existing features
- [x] Performance acceptable (if applicable)
```

**Test Results:**

[Optional: paste coverage report, performance metrics, or screenshots here]

---

## Migration Notes (if applicable)

```text
- Breaking changes: [list any API breaking changes]
- Database migrations required: [yes/no - details if yes]
- Configuration changes needed: [list new/changed config keys]
```

---

## Additional Context

[Extra information that helps reviewers understand the rationale,
alternatives considered, or trade-offs made.]

---

**Author:** [@username]  
**Reviewers Needed:** [@reviewer1], [@reviewer2]  
**Target Branch:** `main` / `develop`
