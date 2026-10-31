import re

INPUT_FILE = "input.txt"
OUTPUT_FILE = "emails.txt"

EMAIL_PATTERN = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"


def main():
    try:
        with open(INPUT_FILE, "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print(f"'{INPUT_FILE}' not found. Please create it in the same folder.")
        return

    emails = sorted(set(re.findall(EMAIL_PATTERN, text)))

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for email in emails:
            f.write(email + "\n")

    print(f"Found {len(emails)} unique email addresses and saved them to '{OUTPUT_FILE}':")
    for email in emails:
        print(" -", email)


if __name__ == "__main__":
    main()