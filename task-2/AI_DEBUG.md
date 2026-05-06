# Task 2 — AI Debugging Report

Document one debugging session you had during Task 1 where you used an LLM
(ChatGPT, Claude, GitHub Copilot, etc.) to help fix a bug.

> ⚠️ **Before pasting code into an LLM:** the `messy_users.csv` data is
> fictional and safe to share. On real-world data at work, never paste names,
> emails, IDs, or other PII into an external LLM. Redact first.

## The Error

<!-- Paste the full traceback or describe the wrong behaviour. Include the
exact error message and the line of your code that triggered it. -->

Traceback (most recent call last):
  File "C:\Users\Gebruiker\c55-data-week1\task-1\src\cleaner.py", line 58, in <module>
    main(args.input, args.output)
  File "C:\Users\Gebruiker\c55-data-week1\task-1\src\cleaner.py", line 46, in main
    cleaned = [c for row in reader if (c := clean_row(row)) is not None]
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Gebruiker\c55-data-week1\task-1\src\cleaner.py", line 46, in <listcomp>
    cleaned = [c for row in reader if (c := clean_row(row)) is not None]
                                            ^^^^^^^^^^^^^^
  File "C:\Users\Gebruiker\c55-data-week1\task-1\src\cleaner.py", line 38, in clean_row
    "salary": clean_salary(row.get("salary", "")),
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Gebruiker\c55-data-week1\task-1\src\utils.py", line 50, in clean_salary
    return int(salary)
           ^^^^^^^^^^^
ValueError: invalid literal for int() with base 10: '62.000'

## The Prompt

<!-- The exact text you sent to the LLM. Include the code you pasted with
it. -->

why do I get an error?



## The Solution

<!-- What did the LLM suggest? Did it work on the first try, or did you
need a follow-up? -->


The error is very clear! The salary value '62.000' cannot be converted to an integer because it has a dot in it.

## Reflection

<!-- A few sentences on: did you understand WHY the original code was
broken, or did you just accept the fix? What would you do differently next
time? -->

62.000 couln't be converted to an interger.Ensure to consider all probabilities of errors occuring when cleaning data
