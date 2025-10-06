# Phase 0: Foundation & Architecture - Action Plan

**Duration**: Weeks 1-4  
**Objective**: Establish solid foundation, clean technical debt, prepare for rapid development

---

## 🎯 **PHASE 0 GOALS**

### **Primary Objectives**
1. ✅ Clean, organized, and documented codebase
2. ✅ Unified architecture that all components follow
3. ✅ Development environment ready for contributors
4. ✅ Foundation for all future phases

### **Success Criteria**
- [ ] Zero empty Python files
- [ ] 100% code passes linting (black, pylint, flake8)
- [ ] All dependencies documented in requirements.txt
- [ ] Clear architecture diagram available
- [ ] New contributors can onboard in < 30 minutes

---

## 📋 **WEEK-BY-WEEK BREAKDOWN**

### **Week 1: Assessment & Planning**

#### **Day 1-2: Repository Audit**
- [ ] Catalog all Python files (count: 218)
- [ ] Catalog all Markdown files (count: 103)
- [ ] Identify empty/placeholder files
- [ ] List duplicate code across branches
- [ ] Map current file structure

#### **Day 3-4: Architecture Design**
- [ ] Document current system components
- [ ] Design unified architecture
- [ ] Create module dependency graph
- [ ] Define clear interfaces between modules
- [ ] Document data flow

#### **Day 5-7: Setup & Standards**
- [ ] Create development environment guide
- [ ] Set up linting tools (black, pylint, flake8)
- [ ] Configure pytest framework
- [ ] Write coding standards document
- [ ] Create Git workflow guide

**Week 1 Deliverables**:
- Repository audit report
- Architecture design document
- Development setup guide
- Coding standards

---

### **Week 2: Cleanup & Organization**

#### **Day 8-9: File Cleanup**
- [ ] Remove all empty Python files
- [ ] Delete unused/obsolete files
- [ ] Remove duplicate code
- [ ] Consolidate similar functionality
- [ ] Update .gitignore for build artifacts

#### **Day 10-11: Code Organization**
- [ ] Reorganize file structure by domain
  ```
  /core              → FANTOM 3D slicer
  /Recur             → Recur framework
  /ghst              → GHST agent system (NEW)
  /shared            → Shared utilities (NEW)
  /tests             → All tests
  /docs              → All documentation
  /scripts           → Build/automation scripts
  /examples          → Usage examples
  ```
- [ ] Fix all import paths
- [ ] Standardize naming conventions
- [ ] Move config files to /config

#### **Day 12-14: Code Quality**
- [ ] Run and fix all linting errors
- [ ] Add type hints to critical functions
- [ ] Remove commented-out code
- [ ] Fix TODO/FIXME items or document them
- [ ] Ensure consistent code style

**Week 2 Deliverables**:
- Clean, organized codebase
- Fixed file structure
- All code passes linting
- Updated imports

---

### **Week 3: Infrastructure & Tooling**

#### **Day 15-16: Development Environment**
- [ ] Create Dockerfile for development
- [ ] Create docker-compose.yml
- [ ] Write setup.sh for Unix/Linux
- [ ] Write setup.bat for Windows
- [ ] Document environment variables

#### **Day 17-18: CI/CD Basics**
- [ ] Set up GitHub Actions workflow
- [ ] Add automated linting check
- [ ] Add automated test runner
- [ ] Configure branch protection rules
- [ ] Set up pre-commit hooks

#### **Day 19-21: Testing Framework**
- [ ] Organize existing tests
- [ ] Create test structure
  ```
  /tests
    /unit         → Unit tests
    /integration  → Integration tests
    /e2e          → End-to-end tests
    /fixtures     → Test data
  ```
- [ ] Write test templates
- [ ] Document testing guidelines
- [ ] Set up code coverage reporting

**Week 3 Deliverables**:
- Docker development environment
- GitHub Actions CI/CD pipeline
- Testing framework ready
- Pre-commit hooks installed

---

### **Week 4: Documentation & Finalization**

#### **Day 22-24: Core Documentation**
- [ ] Update main README.md
  - Project overview
  - Quick start guide
  - Installation instructions
  - Usage examples
  - Contribution guidelines
- [ ] Create ARCHITECTURE.md
  - System overview
  - Component diagram
  - Module descriptions
  - Data flow diagrams
- [ ] Create CONTRIBUTING.md
  - How to contribute
  - Code style guide
  - PR process
  - Issue templates

#### **Day 25-26: API Documentation**
- [ ] Document GHST agent APIs
- [ ] Document FANTOM APIs
- [ ] Document Recur APIs
- [ ] Create API reference template
- [ ] Add docstrings to public functions

#### **Day 27-28: Review & Polish**
- [ ] Final code review
- [ ] Test all setup scripts
- [ ] Verify documentation accuracy
- [ ] Create onboarding checklist
- [ ] Prepare Phase 1 kickoff

**Week 4 Deliverables**:
- Complete documentation
- Onboarding guide
- Phase 0 completion report
- Ready for Phase 1

---

## 🗂️ **FILE STRUCTURE TARGET**

```
BLEND-RECURse/
├── README.md                           ← Main project overview
├── PROJECT_GOAL_AND_ROADMAP.md         ← Detailed roadmap
├── ROADMAP_QUICK_REFERENCE.md          ← Quick reference
├── PHASE_0_ACTION_PLAN.md              ← This file
├── LICENSE                             ← MIT License
├── .gitignore                          ← Git ignore rules
├── requirements.txt                    ← Python dependencies
├── setup.py                            ← Package setup
├── Dockerfile                          ← Development container
├── docker-compose.yml                  ← Multi-container setup
├── .github/
│   ├── workflows/
│   │   ├── ci.yml                      ← CI/CD pipeline
│   │   └── release.yml                 ← Release automation
│   ├── ISSUE_TEMPLATE/
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── CONTRIBUTING.md
├── config/                             ← Configuration files
│   ├── default.yaml
│   └── development.yaml
├── core/                               ← FANTOM 3D Slicer
│   ├── README.md
│   ├── src/
│   │   ├── slicer_ui/
│   │   ├── ai_collaboration/
│   │   └── utils/
│   └── tests/
├── Recur/                              ← Recur Framework
│   ├── README.md
│   ├── agents/
│   ├── plugins/
│   ├── api/
│   ├── ui/
│   └── tests/
├── ghst/                               ← GHST Agent System (NEW)
│   ├── README.md
│   ├── agents/
│   │   ├── ghost_manager.py
│   │   └── ghost_chat.py
│   ├── council/
│   ├── upi/                            ← Universal Programming Interface
│   └── tests/
├── shared/                             ← Shared Utilities (NEW)
│   ├── utils/
│   ├── config/
│   └── tests/
├── docs/                               ← Documentation
│   ├── ARCHITECTURE.md
│   ├── API_REFERENCE.md
│   ├── INSTALLATION.md
│   ├── USER_GUIDE.md
│   ├── CONTRIBUTING.md
│   └── tutorials/
├── tests/                              ← Integration/E2E tests
│   ├── integration/
│   └── e2e/
├── scripts/                            ← Build/automation scripts
│   ├── setup.sh
│   ├── setup.bat
│   ├── lint.sh
│   └── test.sh
├── examples/                           ← Usage examples
│   ├── basic_usage/
│   ├── advanced_features/
│   └── plugins/
└── releases/                           ← Release artifacts
    └── archive/                        ← Old releases (archived)
```

---

## 🔧 **TECHNICAL TASKS**

### **Task 1: Codebase Cleanup Script**

Create `scripts/cleanup_codebase.py`:

```python
"""
Automated codebase cleanup script for Phase 0
Removes empty files, fixes common issues, reports problems
"""

import os
import sys
from pathlib import Path

def find_empty_python_files(root_dir):
    """Find all empty or nearly empty Python files."""
    empty_files = []
    for path in Path(root_dir).rglob("*.py"):
        if path.stat().st_size == 0:
            empty_files.append(str(path))
        else:
            # Check if file only has comments/whitespace
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read().strip()
                # Remove comments and whitespace
                lines = [l.strip() for l in content.split('\n') 
                        if l.strip() and not l.strip().startswith('#')]
                if len(lines) == 0:
                    empty_files.append(str(path))
    return empty_files

def find_duplicate_imports(root_dir):
    """Find files with duplicate import statements."""
    # Implementation here
    pass

def main():
    root_dir = Path(__file__).parent.parent
    
    print("🔍 Scanning codebase...")
    
    # Find empty files
    empty_files = find_empty_python_files(root_dir)
    print(f"\n📄 Found {len(empty_files)} empty Python files:")
    for f in empty_files[:10]:  # Show first 10
        print(f"  - {f}")
    
    # More checks...
    
    print("\n✅ Cleanup scan complete!")
    print(f"Total issues found: {len(empty_files)}")

if __name__ == "__main__":
    main()
```

### **Task 2: Linting Configuration**

Create `pyproject.toml`:

```toml
[tool.black]
line-length = 100
target-version = ['py310']
include = '\.pyi?$'
extend-exclude = '''
/(
    \.git
  | \.venv
  | build
  | dist
  | releases
)/
'''

[tool.pylint.messages_control]
disable = "C0330, C0326"

[tool.pylint.format]
max-line-length = 100

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py", "*_test.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
addopts = "-v --cov=. --cov-report=html --cov-report=term"
```

### **Task 3: GitHub Actions CI**

Create `.github/workflows/ci.yml`:

```yaml
name: CI Pipeline

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main, develop ]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: |
          pip install black pylint flake8
      - name: Run black
        run: black --check .
      - name: Run pylint
        run: pylint **/*.py
      - name: Run flake8
        run: flake8 .

  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install pytest pytest-cov
      - name: Run tests
        run: pytest
```

### **Task 4: Pre-commit Hooks**

Create `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 23.1.0
    hooks:
      - id: black
        language_version: python3.10

  - repo: https://github.com/pycqa/flake8
    rev: 6.0.0
    hooks:
      - id: flake8
        args: [--max-line-length=100]

  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files
```

---

## 📊 **PROGRESS TRACKING**

### **Daily Standup Questions**
1. What did you complete yesterday?
2. What will you work on today?
3. Any blockers or issues?

### **Weekly Review Checklist**
- [ ] All planned tasks completed?
- [ ] Any unexpected issues discovered?
- [ ] Documentation updated?
- [ ] Tests passing?
- [ ] Ready for next week?

### **Phase 0 Completion Checklist**

#### **Architecture**
- [ ] Architecture document created
- [ ] Component diagram drawn
- [ ] Module interfaces defined
- [ ] Data flow documented
- [ ] Dependency map created

#### **Code Quality**
- [ ] Empty files removed
- [ ] Duplicate code consolidated
- [ ] Linting errors fixed (0 errors)
- [ ] Type hints added to critical functions
- [ ] Consistent code style

#### **Infrastructure**
- [ ] Docker environment working
- [ ] CI/CD pipeline operational
- [ ] Pre-commit hooks installed
- [ ] Testing framework ready
- [ ] Code coverage > 50%

#### **Documentation**
- [ ] README.md updated
- [ ] ARCHITECTURE.md created
- [ ] CONTRIBUTING.md written
- [ ] API documentation started
- [ ] Onboarding guide complete

---

## 🚀 **GETTING STARTED TODAY**

### **Step 1: Clone and Explore** (15 mins)
```bash
git clone https://github.com/allanwrench28/BLEND-RECURse.git
cd BLEND-RECURse
ls -la  # Explore structure
```

### **Step 2: Audit Current State** (30 mins)
```bash
# Count files
find . -name "*.py" | wc -l
find . -name "*.md" | wc -l

# Find empty files
find . -name "*.py" -size 0

# Check for TODO/FIXME
grep -r "TODO\|FIXME" --include="*.py" .
```

### **Step 3: Set Up Dev Environment** (45 mins)
```bash
# Install dependencies
pip install -r requirements.txt

# Install dev tools
pip install black pylint flake8 pytest pytest-cov

# Run initial checks
black --check .
pylint **/*.py || true  # May have errors initially
pytest || true  # May have failures initially
```

### **Step 4: Create GitHub Issues** (30 mins)
- Create issues for each Phase 0 task
- Add to Phase 0 milestone
- Assign to team members
- Add labels (cleanup, documentation, infrastructure)

### **Step 5: Start First Task** (Rest of day)
- Pick highest priority task
- Create feature branch
- Make changes
- Test locally
- Submit PR

---

## 💡 **TIPS FOR SUCCESS**

### **For the Team**
1. ✅ **Communicate early and often** - Daily updates in chat
2. ✅ **Small, frequent PRs** - Don't wait to merge everything at once
3. ✅ **Document as you go** - Don't leave docs for the end
4. ✅ **Test your changes** - Ensure code works before PR
5. ✅ **Ask for help** - Don't stay blocked

### **Common Pitfalls to Avoid**
1. ❌ **Scope creep** - Stick to Phase 0 goals only
2. ❌ **Perfectionism** - Good enough is good enough for Phase 0
3. ❌ **Analysis paralysis** - Make decisions and move forward
4. ❌ **Working in isolation** - Collaborate and communicate
5. ❌ **Ignoring tech debt** - This is the time to fix it!

---

## 📞 **NEED HELP?**

- **Questions?** Open a GitHub Discussion
- **Bugs?** Create a GitHub Issue
- **Ideas?** Share in Discussions
- **Blocked?** Tag project lead in issue

---

## 🎉 **PHASE 0 COMPLETION**

When Phase 0 is complete, you'll have:

✅ **Clean Codebase** - Organized, linted, documented  
✅ **Solid Foundation** - Architecture, standards, tools  
✅ **Happy Team** - Clear guidelines, easy onboarding  
✅ **Ready for Phase 1** - Build AI agents on solid base  

**Let's build this foundation together!** 🚀

---

*Action Plan Version: 1.0*  
*Part of BLEND-RECURse Roadmap*  
*See PROJECT_GOAL_AND_ROADMAP.md for full details*
