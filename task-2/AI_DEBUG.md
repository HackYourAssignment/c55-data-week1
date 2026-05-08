# Task 2 — AI Debugging Report

Document one debugging session you had during Task 1 where you used an LLM
(ChatGPT, Claude, GitHub Copilot, etc.) to help fix a bug.

> ⚠️ **Before pasting code into an LLM:** the `messy_users.csv` data is
> fictional and safe to share. On real-world data at work, never paste names,
> emails, IDs, or other PII into an external LLM. Redact first.

## The Error

<!-- Paste the full traceback or describe the wrong behaviour. Include the
exact error message and the line of your code that triggered it. -->
While working on Task 1, my first version of `clean_salary()` tried to convert the salary directly to an integer after removing commas and quotes. It worked for values like `85000` and `"68,000"`, but it crashed when the CSV contained an unexpected salary format with a period inside the value.

My first version was:

def clean_salary(raw: str) -> int | None:
    """Parse a messy salary cell into an int.

    Handles inputs like "85000", "  95000", '"68,000"', "N/A", "".
    Returns None when the value cannot be parsed (missing or "N/A").
    """
    salary = raw.strip()
    if salary in ("", "N/A"):
        return None

    salary = salary.replace('"', "")
    salary = salary.replace(",", "")
    salary = salary.strip()

    return int(salary)

When I ran the cleaner:

python3 src/cleaner.py --input data/messy_users.csv --output output/clean_users.json

I got this traceback:

Traceback (most recent call last):
  File "G:\Halyna_work\traineeship_Amsterdam\Data-track\week-1\c55-data-week1\task-1\src\cleaner.py", line 58, in <module>
    main(args.input, args.output)
  File "G:\Halyna_work\traineeship_Amsterdam\Data-track\week-1\c55-data-week1\task-1\src\cleaner.py", line 46, in main
    cleaned = [c for row in reader if (c := clean_row(row)) is not None]
                                            ^^^^^^^^^^^^^^
  File "G:\Halyna_work\traineeship_Amsterdam\Data-track\week-1\c55-data-week1\task-1\src\cleaner.py", line 38, in clean_row
    "salary": clean_salary(row.get("salary", "")),
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "G:\Halyna_work\traineeship_Amsterdam\Data-track\week-1\c55-data-week1\task-1\src\utils.py", line 55, in clean_salary
    return int(salary)
           ^^^^^^^^^^^
ValueError: invalid literal for int() with base 10: '62.000'

The problem was that int() can only parse strings that look like valid integers, for example "62000". It cannot parse "62.000".

## The Prompt

<!-- The exact text you sent to the LLM. Include the code you pasted with
it. -->
I am working on a beginner Python CSV cleaning task.

The cleaner reads rows from messy_users.csv and calls this helper function:

def clean_salary(raw: str) -> int | None:
    salary = raw.strip()

    if salary == "":
        return None

    if salary.lower() == "n/a":
        return None

    salary = salary.replace('"', "")
    salary = salary.replace(",", "")

    return int(salary)

The assignment says:
- salaries like "85000", " 95000", and '"68,000"' should become integers
- empty values and "N/A" should become None
- if the value cannot be parsed, the function should return None instead of crashing

When I run the script, I get this error:

ValueError: invalid literal for int() with base 10: '62.000'

How should I fix clean_salary so the script keeps running?

## The Solution

<!-- What did the LLM suggest? Did it work on the first try, or did you
need a follow-up? -->
The AI suggested wrapping the final int(salary) conversion in a try/except ValueError block. It also suggested keeping the cleaning steps for whitespace, quotes, and commas before the conversion.

The fixed function was:

def clean_salary(raw: str) -> int | None:
    salary = raw.strip()
    if salary in ("", "N/A"):
        return None

    salary = salary.replace('"', "")
    salary = salary.replace(",", "")
    salary = salary.strip()

    try:
        return int(salary)
    except ValueError:
        return None

This worked after I reran the command:

python3 src/cleaner.py --input data/messy_users.csv --output output/clean_users.json

The script no longer crashed. Instead, rows with invalid salary formats were still included in the output, but their "salary" value became null in the JSON file.

## Reflection

<!-- A few sentences on: did you understand WHY the original code was
broken, or did you just accept the fix? What would you do differently next
time? -->
I understood why the original code was broken. The mistake was assuming that every non-empty and non-N/A salary could be converted with int(). That assumption was too strong because real CSV data can contain unexpected formats.

I did not need to change cleaner.py, because the orchestration logic was already correct. The bug belonged inside the helper function that parsed one field.

Next time, I would test helper functions separately before running the whole script. For example, I would manually check:

clean_salary("85000")
clean_salary('"68,000"')
clean_salary("N/A")
clean_salary("")
clean_salary("62.000")

That would catch the parsing problem earlier and make the traceback easier to understand.
