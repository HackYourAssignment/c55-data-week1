# Task 2 — AI Debugging Report

Document one debugging session you had during Task 1 where you used an LLM
(ChatGPT, Claude, GitHub Copilot, etc.) to help fix a bug.

> ⚠️ **Before pasting code into an LLM:** the `messy_users.csv` data is
> fictional and safe to share. On real-world data at work, never paste names,
> emails, IDs, or other PII into an external LLM. Redact first.

## The Error

I ran the script and got this error:

```
ValueError: invalid literal for int() with base 10: '85000.50'
```

I didn't understand what was happening at first. The traceback was long and confusing. I think it happened somewhere in my `clean_salary` function but I wasn't sure. I ran the script again and got the same error. The salary value `"85000.50"` has a decimal point and `int()` doesn't like that I guess?

## The Prompt

I searched online and asked ChatGPT:

"why does my code crash with ValueError when trying to convert salary to int? here is the error:

```
ValueError: invalid literal for int() with base 10: '85000.50'
```

and my function:

```python
def clean_salary(raw: str) -> int | None:
    cleaned = raw.strip().replace('"', "").replace(",", "")
    if cleaned == "" or cleaned.upper() == "N/A":
        return None
    return int(cleaned)
```

what am i doing wrong?"

I also pasted some examples from the CSV: `"85000.50"`, `"68,000"`, `N/A`, blank cells

## The Solution

ChatGPT told me to use try/except:

```python
try:
    return int(cleaned)
except ValueError:
    return None
```

It said: "ValueError is thrown when int() can't convert the string. Use try/except to catch it and return None instead of crashing."

I added this to my code and ran it again. It worked! No more error. The script finished and created the JSON file with 12 rows. Some salaries are now null but that's ok I think because the data was bad anyway.


## Reflection

Honestly, I just accepted the fix because it worked and moved on. I didn't really think about WHY int() was breaking. I guess it can't handle decimals? Or commas? I'm not totally sure.

I probably should have read the task more carefully at the start. It did say "expect at least one row to break your first attempt" so I wasn't really thinking about error handling from the beginning. I just wrote the simplest code and then it broke.

The try/except thing is useful. I'll probably use it more in the future when I expect things might fail. 