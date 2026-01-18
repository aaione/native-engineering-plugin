# Knowledge Taxonomy & Search Guide

This file defines the standards for indexing and searching project memory. Use this to formulate effective queries.

## 1. Problem Categories (Context Filters)

When searching `knowledge-index.json`, filter by these `category` values:

- **build-errors**: CI/CD, compilation, packaging.
- **test-failures**: Flaky tests, RSpec/Minitest config, factory issues.
- **runtime-errors**: Crashes, exceptions (StandardError, RuntimeError).
- **performance-issues**: Memory, CPU, DB latency, O(n), N+1.
- **database-issues**: Migrations, SQL, indexes, locking, Active Record.
- **security-issues**: Auth, CORS, XSS, leaked secrets, permissions.
- **ui-bugs**: CSS/Layout, Stimulus JS, Turbo navigation, Responsive.
- **integration-issues**: Stripe, AWS, External APIs, Webhooks.
- **logic-errors**: State machines, business rules, calculators.
- **developer-experience**: Tooling, local setup, Docker, Scripts.
- **workflow-issues**: Branching, PR process, code review loops.
- **best-practices**: Reusable patterns and "The Right Way".
- **documentation-gaps**: Missing context in README/CLAUDE.md.

## 2. Technical Tags (Core Intersections)

Common technical intersections to look for in `tag_index`:

- **Platform**: `rails`, `nextjs`, `react`, `ios`, `android`.
- **Persistence**: `postgres`, `redis`, `elasticsearch`, `s3`.
- **Frontend**: `stimulus`, `turbo`, `tailwind`, `typescript`.
- **Patterns**: `eager-loading`, `idempotency`, `singleton`, `orchestrator`.

## 3. Error Signature Heuristics

The `error_index` automatically captures patterns matching `[A-Z]\w+Error`. 
Common signatures to search:
- `ActiveRecord::RecordNotFound`
- `Redis::TimeoutError`
- `ActionController::ParameterMissing`
- `NoMethodError`
- `NameError`

## 4. Search Best Practices

1. **Start Precise**: Search for the exact `ErrorName` first.
2. **Expand to Tags**: If no error match, search for the `technology` (e.g., `redis`).
3. **Keyword Fallback**: Use `keyword_index` for functional themes (e.g., `caching`, `upload`, `auth`).
