"""Pure helper functions for cleaning individual fields of messy_users.csv.

Each function takes the raw string from the CSV and returns the cleaned
value (or `None` for missing-but-valid). They never read or write files;
keep them pure so they are easy to test.
"""

from __future__ import annotations


def clean_name(raw: str) -> str:
    return raw.strip()


def clean_email(raw: str) -> str:
    
    return raw.strip().lower()


def clean_department(raw: str) -> str:
    cleaned = raw.strip()
    return cleaned if cleaned else "Unknown"


def clean_salary(raw: str) -> int | None:
    """Parse a messy salary cell into an int.

    Handles inputs like "85000", "  95000", '"68,000"', "N/A", "".
    Returns None when the value cannot be parsed (missing or "N/A").
    """
    cleaned = raw.strip().replace(",", "").replace('"', "")
    if not cleaned or cleaned.upper() == "N/A":
        return None
    
    try:
        return int(cleaned) 
    except ValueError:
     return None
    