import re


def extract_emails(input_file, output_file):
    """Extract email addresses from a text file and save them to another file."""

    try:
        # Read the input file
        with open(input_file, "r", encoding="utf-8") as file:
            text = file.read()

        # Find email addresses using regular expression
        emails = re.findall(
            r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
            text
        )

        # Remove duplicate emails
        unique_emails = sorted(set(emails))

        # Save emails to output file
        with open(output_file, "w", encoding="utf-8") as file:
            for email in unique_emails:
                file.write(email + "\n")

        print("\n====================================")
        print("       EMAIL EXTRACTION COMPLETE")
        print("====================================")
        print(f"Emails found: {len(unique_emails)}")
        print(f"Saved to: {output_file}")
        print("====================================")

    except FileNotFoundError:
        print(f"\nError: {input_file} was not found.")

    except Exception as error:
        print(f"\nAn unexpected error occurred: {error}")


def main():
    input_file = "input.txt"
    output_file = "emails.txt"

    print("====================================")
    print("       EMAIL EXTRACTOR")
    print("====================================")

    extract_emails(input_file, output_file)


if __name__ == "__main__":
    main()