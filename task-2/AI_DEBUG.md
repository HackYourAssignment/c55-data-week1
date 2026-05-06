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
  File "/Users/barbari/Desktop/c55-data-week1/task-1/src/cleaner.py", line 17, in <module>
    from utils import clean_department, clean_email, clean_name, clean_salary
  File "/Users/barbari/Desktop/c55-data-week1/task-1/src/utils.py", line 65
    expect ValueError:
    ^^^^^^

## The Prompt

<!-- The exact text you sent to the LLM. Include the code you pasted with
it. -->
I paseted the following error and code :

I am getting an error in my Python script.
What is the problem 
This is the code : 

try:
    return int(salary)
expect ValueError:
    return None


## The Solution

<!-- What did the LLM suggest? Did it work on the first try, or did you
need a follow-up? -->
The problem is a simple typo in your exception handling:

expect ValueError:

should be:

except ValueError:

So your corrected code is:

try:
    return int(salary)
except ValueError:
    return None

That’s it—except is the correct Python keyword.

yes it worked immediatly
## Reflection

<!-- A few sentences on: did you understand WHY the original code was
broken, or did you just accept the fix? What would you do differently next
time? -->
yes, the real issue was a syntax error. python doesnt recognize expect, only except so the code coudnt run at all .
next time i will focus on the syntax .


