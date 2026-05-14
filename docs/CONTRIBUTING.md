# Contributing to LQDOJ

## Git Workflow

### Repository Setup

This fork uses two remotes:

- **origin**: Upstream LQDJudge repository (https://github.com/LQDJudge/online-judge.git)
- **ks2n**: Personal fork (git@github.com:ks2n/online-judge.git)

### Commit Practice

**IMPORTANT**: Commit after each logical change. Do not accumulate multiple unrelated changes.

```bash
# After making a change:
git add <files>
git commit -m "<type>: <description>"
```

### Commit Message Format

Follow conventional commits:

```
<type>: <description>

<optional body>
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `refactor`: Code refactoring
- `docs`: Documentation
- `style`: Formatting, SCSS changes
- `test`: Adding tests
- `chore`: Maintenance tasks

**Examples:**
```
feat: add difficulty badge to problem list
fix: resolve mobile menu overflow on small screens
style: update edu theme color tokens
refactor: extract problem card component
docs: add git workflow documentation
```

### Sync and Push Workflow

```bash
# 1. Fetch upstream changes
git fetch origin

# 2. Merge upstream into local
git merge origin/master

# 3. Resolve conflicts if any
git add <resolved-files>
git commit -m "merge: sync with upstream"

# 4. Push to personal fork
git push ks2n master
```

### When to Commit

Commit after:
- Adding a new feature or component
- Fixing a bug
- Refactoring code
- Updating documentation
- Changing SCSS/CSS
- Modifying templates
- Database migrations

**Do NOT wait to accumulate multiple changes before committing.**

## Development Workflow

### 1. SCSS Changes

```bash
# Edit SCSS files in resources/ directory
# Then build inside Docker container:
docker compose -f .docker/dev-local/docker-compose.yml exec web bash -c \
  "cd /code && bash make_style.sh && python3 manage.py collectstatic --noinput"

# Commit the changes:
git add resources/
git commit -m "style: update button styles in edu theme"
```

### 2. Template Changes

```bash
# Edit template files in templates/ directory
# Test in browser at http://localhost:8001

# Commit the changes:
git add templates/
git commit -m "feat: add learning dashboard to home page"
```

### 3. Backend Changes

```bash
# Edit Python files (views, models, forms, etc.)
# Restart web service:
docker compose -f .docker/dev-local/docker-compose.yml restart web

# Run tests if applicable:
docker compose -f .docker/dev-local/docker-compose.yml exec web python3 manage.py test

# Commit the changes:
git add judge/
git commit -m "feat: add difficulty badge filter"
```

### 4. Database Migrations

```bash
# Create migrations:
docker compose -f .docker/dev-local/docker-compose.yml exec web python3 manage.py makemigrations

# Apply migrations:
docker compose -f .docker/dev-local/docker-compose.yml exec web python3 manage.py migrate

# Commit migrations:
git add judge/migrations/
git commit -m "feat: add problem attachment model"
```

## Code Quality

### Before Committing

- [ ] Code follows project conventions (see `.claude/rules/` for details)
- [ ] SCSS changes are built and tested
- [ ] Templates are tested in browser
- [ ] Backend changes are tested with dev server
- [ ] No console.log or debug statements left in code
- [ ] Commit message follows conventional commits format

### Testing

```bash
# Run Django tests:
docker compose -f .docker/dev-local/docker-compose.yml exec web python3 manage.py test

# Visual regression testing (if significant UI changes):
node e2e-audit/baseline-audit.mjs
```

## Docker Development

All development happens inside Docker containers. See [docker-workflow.md](../.claude/rules/docker-workflow.md) for detailed Docker commands.

### Quick Reference

```bash
# Start services:
cd .docker/dev-local/
docker compose up -d

# View logs:
docker compose logs -f web

# Run Django commands:
docker compose exec web python3 manage.py <command>

# Build SCSS:
docker compose exec web bash -c "cd /code && bash make_style.sh"

# Restart services:
docker compose restart web
```

## Edu Theme Development

The edu theme is a modern, friendly design system inspired by Brilliant.org and Duolingo. See [edu-design-system.md](./edu-design-system.md) for complete design guidelines.

### Key Principles

- Token-first approach: change `vars.scss` values instead of writing overrides
- All edu overrides use `body.edu` prefix for specificity
- Mobile-first responsive design
- Accessibility-compliant (WCAG AA)

### File Organization

```
resources/
├── edu-theme.scss     ← Entry point
├── edu/               ← Theme partials
│   ├── _tokens.scss
│   ├── _navigation.scss
│   ├── _components.scss
│   └── ...
├── vars.scss          ← Token palette (single source of truth)
└── *.scss             ← Legacy SCSS
```

## Questions?

For detailed conventions, see:
- [Django conventions](../.claude/rules/django-conventions.md)
- [SCSS conventions](../.claude/rules/scss-conventions.md)
- [Template conventions](../.claude/rules/template-conventions.md)
- [Docker workflow](../.claude/rules/docker-workflow.md)
