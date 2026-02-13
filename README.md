# Bug Automation POC

🤖 Automated bug fixing workflow integrating Jira and GitHub

## What This Does

This is a Proof of Concept (POC) that demonstrates an automated workflow for:
1. Detecting new bugs in Jira
2. Analyzing the bug automatically
3. Creating a code fix
4. Writing automated tests
5. Creating a Pull Request
6. Running tests on staging after merge
7. Updating Jira with results

## Project Structure

```
bug-automation-poc/
├── calculator.py           # Simple Python calculator (with intentional bugs)
├── test_calculator.py      # Unit tests for the calculator
├── requirements.txt        # Python dependencies
├── .github/
│   └── workflows/
│       └── bug-fix-automation.yml  # Main automation workflow
└── README.md              # This file
```

## Intentional Bugs for Testing

The calculator has two intentional bugs:

1. **Division by Zero**: The `divide()` method crashes when dividing by zero
2. **Square Root of Negative**: The `sqrt()` method crashes for negative numbers

## How to Use

### Manual Testing

1. Create a bug in Jira with details about one of the bugs
2. Go to GitHub → Actions → "Bug Fix Automation"
3. Click "Run workflow"
4. Enter the Jira issue key (e.g., "BAP-1")
5. Watch the magic happen! ✨

### What Happens

1. ✅ Fetches bug details from Jira
2. ✅ Updates Jira status to "In Progress"
3. ✅ Analyzes the bug
4. ✅ Creates a fix
5. ✅ Writes/updates tests
6. ✅ Creates a Pull Request
7. ✅ Adds comment to Jira with PR link
8. ✅ After PR merge: deploys to staging
9. ✅ Runs automated tests
10. ✅ Updates Jira to "Testing Complete"

## Setup Instructions

See `COMPLETE_POC_SETUP_GUIDE.md` for detailed setup instructions.

## Requirements

- Python 3.11+
- GitHub account
- Jira account (free tier works)
- GitHub App configured

## Testing the Bugs Manually

```bash
# Install dependencies
pip install -r requirements.txt

# Run tests (some will fail initially)
python -m pytest test_calculator.py -v

# Run the calculator demo
python calculator.py
```

## Sample Jira Bug Reports

### Bug 1: Division by Zero
```
Summary: Calculator divide by zero error
Description:
When calling calculator.divide(10, 0), the program crashes.

Expected: Should handle gracefully
Actual: ZeroDivisionError

File: calculator.py
Function: divide
```

### Bug 2: Square Root of Negative
```
Summary: Calculator sqrt of negative number fails
Description:
When calling calculator.sqrt(-4), the program raises ValueError.

Expected: Should handle gracefully
Actual: ValueError: math domain error

File: calculator.py
Function: sqrt
```

## Architecture

```
┌─────────────┐
│    Jira     │ New bug created
│   (Issue)   │
└──────┬──────┘
       │
       │ (Manual trigger for POC)
       │
       ▼
┌─────────────────────────────────────┐
│     GitHub Actions Workflow         │
│                                     │
│  1. Fetch issue from Jira           │
│  2. Analyze bug                     │
│  3. Generate fix                    │
│  4. Run tests                       │
│  5. Create PR                       │
│  6. Update Jira                     │
└─────────────┬───────────────────────┘
              │
              ▼
       ┌──────────────┐
       │ Pull Request │ ← You review here
       └──────┬───────┘
              │ (After merge)
              ▼
       ┌──────────────┐
       │   Staging    │
       │ Deployment   │
       └──────┬───────┘
              │
              ▼
       ┌──────────────┐
       │ Update Jira  │
       │  (Complete)  │
       └──────────────┘
```

## Future Enhancements

- [ ] Use Claude AI for smarter bug analysis
- [ ] Automatic webhook integration (no manual trigger)
- [ ] Support for more programming languages
- [ ] Integration with actual staging environment
- [ ] Screenshot capture of fixes working
- [ ] Slack notifications
- [ ] Metrics and analytics dashboard

## License

MIT

## Questions?

Check the `COMPLETE_POC_SETUP_GUIDE.md` for troubleshooting and detailed setup instructions.

---

🤖 Built with automation in mind
