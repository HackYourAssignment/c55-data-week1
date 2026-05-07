# Task 2 — AI Debugging Report

Document one debugging session you had during Task 1 where you used an LLM
(ChatGPT, Claude, GitHub Copilot, etc.) to help fix a bug.

> ⚠️ **Before pasting code into an LLM:** the `messy_users.csv` data is
> fictional and safe to share. On real-world data at work, never paste names,
> emails, IDs, or other PII into an external LLM. Redact first.

## The Error

<!-- Paste the full traceback or describe the wrong behaviour. Include the
exact error message and the line of your code that triggered it. -->

During Task 1, I encountered two main issues. First, an accidental import was added:
`from curses import raw`
This caused potential environment errors. Second, the `clean_salary` function did not return a value in all cases.  
If the input was not a digit, the function would exit without returning anything, which caused unexpected behavior.

## The Prompt

<!-- The exact text you sent to the LLM. Include the code you pasted with
it. -->

I asked ChatGPT:

"My function clean_salary sometimes doesn't return a value. Here is my code:

def clean_salary(raw: str) -> int | None:
    cleaned = raw.strip().replace(',', '')
    if cleaned.isdigit():
        return int(cleaned)

Why is it failing and how can I fix it?"

## The Solution

<!-- What did the LLM suggest? Did it work on the first try, or did you
need a follow-up? -->

The AI explained that my function was missing a return statement for cases where the input is not a valid number.

It suggested adding:

return None

at the end of the function.

After adding this line, the function worked correctly on all test cases.

## Reflection

<!-- A few sentences on: did you understand WHY the original code was
broken, or did you just accept the fix? What would you do differently next
time? -->

I understood that the problem was caused by missing return paths in my function.  
At first, I just followed the AI suggestion, but then I realized that in Python every condition must return a value or the function will return None implicitly.

Next time, I will first check all possible input cases myself before asking AI for help.
