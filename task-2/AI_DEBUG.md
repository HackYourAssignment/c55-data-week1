# Task 2 — AI Debugging Report

Document one debugging session you had during Task 1 where you used an LLM
(ChatGPT, Claude, GitHub Copilot, etc.) to help fix a bug.

> ⚠️ **Before pasting code into an LLM:** the `messy_users.csv` data is
> fictional and safe to share. On real-world data at work, never paste names,
> emails, IDs, or other PII into an external LLM. Redact first.

## The Error

During Task 1, my first version of `clean_salary` removed commas but did not safely handle invalid salary values.

## The Prompt

I'm cleaning salary values from a CSV.

The inputs can look like "85000", " 95000", '"68,000"', "N/A", or empty strings.
I want to return an int when possible, or None for missing/invalid values.

Is this function safe, or could it crash on certain inputs?

```python
def clean_salary(raw: str) -> int | None:
    cleaned = raw.strip().replace(",", "")
    if not cleaned or cleaned.upper() == "N/A":
        return None
    return int(cleaned)
```

## The Solution

ChatGPT explained that my function could crash because int(cleaned) was not inside a try/except block. It also pointed out that I should remove quote characters as well as commas.

the suggested fix:

```python
def clean_salary(raw: str) -> int | None:
    cleaned = raw.strip()

    if not cleaned or cleaned.upper() == "N/A":
        return None

    cleaned = cleaned.replace('"', "").replace(",", "")

    try:
        return int(cleaned)
    except ValueError:
        return None
```

## Reflection

understand why the original code was broken. The CSV values are strings, and not every salary string can safely be converted directly with int(). Values like "68,000", N/A, empty strings, or unexpected formats can cause problems. Next time, I would test my helper function with several messy examples before running the full script, especially when converting strings into numbers.
