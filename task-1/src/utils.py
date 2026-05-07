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
    department = raw.strip()
    if department == "":
        return "Unknown"
    return department


def clean_salary(raw: str) -> int | None:
    cleaned = raw.strip().replace('"', "").replace(",", "")
    if cleaned == "" or cleaned.upper() == "N/A":
        return None
    try:
        return int(cleaned)
    except ValueError:
        return None
