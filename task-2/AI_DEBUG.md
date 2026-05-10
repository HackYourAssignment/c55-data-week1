# Task 2 — AI Debugging Report

Document one debugging session you had during Task 1 where you used an LLM
(ChatGPT, Claude, GitHub Copilot, etc.) to help fix a bug.

> ⚠️ **Before pasting code into an LLM:** the `messy_users.csv` data is
> fictional and safe to share. On real-world data at work, never paste names,
> emails, IDs, or other PII into an external LLM. Redact first.

## The Error

python src/cleaner.py --input data/messy_users.csv --output output/clean_users.json
Traceback (most recent call last):
File "C:\Users\Bader\Desktop\d1\c55-data-week1\task-1\src\cleaner.py", line 17, in <module>
from utils import clean_department, clean_email, clean_name, clean_salary
File "C:\Users\Bader\Desktop\d1\c55-data-week1\task-1\src\utils.py", line 56
cleaned = raw.strip().replace(",", "").replace('"', "")
^
IndentationError: unindent does not match any outer indentation level

## The Prompt

if not raw.strip() or raw.strip().lower() == "n/a":

        return None

    cleaned = raw.strip().replace(",", "").replace('"', "")

if cleaned.isdigit():

        return int(cleaned)

File "C:\Users\Bader\Desktop\d1\c55-data-week1\task-1\src\cleaner.py", line 17, in <module>

    from utils import clean_department, clean_email, clean_name, clean_salary

File "C:\Users\Bader\Desktop\d1\c55-data-week1\task-1\src\utils.py", line 56

    cleaned = raw.strip().replace(",", "").replace('"', "")

                                                           ^

IndentationError: unindent does not match any outer indentation level

## The Solution

It looks like you've hit one of the most common (and admittedly frustrating) rites of passage in Python: the IndentationError.

In Python, whitespace isn't just for readability; it's part of the syntax. This specific error means your code's spacing is inconsistent—likely a mix of tabs and spaces, or a line that shifted slightly out of alignment with the rest of its block.
The Fix

Looking at your snippet, the lines following the if statement need to be consistently indented. Here is the corrected structure:
Python

def clean_salary(raw):
    if not raw.strip() or raw.strip().lower() == "n/a":
        return None
    
    # Ensure this line is aligned with the 'if' above it
    cleaned = raw.strip().replace(",", "").replace('"', "")
    
    # Ensure this block is aligned correctly
    if cleaned.isdigit():
        return int(cleaned)

Common Culprits

    Tabs vs. Spaces: This is the #1 cause. If line 1 uses four spaces and line 2 uses one tab, Python will throw this error even if they look aligned on your screen.

        Pro Tip: Set your editor (VS Code, PyCharm, etc.) to "Indent using Spaces" and "Render Whitespace" so you can see the invisible dots or arrows.

    The "Ghost" Space: Sometimes a single accidental space creeps in at the start of a line.

    Copy-Paste Issues: If you copied this logic from a website or another file, the indentation depth might have changed relative to the function it was pasted into.

How to Resolve This Quickly

If you are using VS Code:

    Select all the text in utils.py.

    Open the Command Palette (Ctrl+Shift+P).

    Type "Convert Indentation to Spaces" and hit Enter.

    Manually re-align the lines to ensure they sit at the same level.

Your logic itself—stripping commas and quotes to turn a string into an integer—is solid! Just give those margins a quick polish and you should be good to go.

## Reflection

i did understand how indentation work (kind of! still alittle bit confusing) and it lead me to think of prettier for javascript and an alternative for python which lead me to "black / ruff" which i decided to install ruff [made my life much easier] and ask about both next lesson :D 
