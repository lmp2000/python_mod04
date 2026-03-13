import sys


def crisis_handler(file_name: str) -> None:
    try:
        with open(file_name) as f:
            print(
                f"\nROUTINE ACCESS: Attempting access to {f.name}..."
            )
            content = f.read()
            sys.stdout.write(
                f"SUCCESS: Archive recovered -``{content}''\n"
            )
            sys.stdout.write(
                'STATUS: Normal operations resumed\n'
            )
    except FileNotFoundError:
        print(
        f"\nCRISIS ALERT: Attempting access to'{file_name}'..."
    )
        sys.stderr.write(
            'RESPONSE: Archive not found in storage matrix\n'
            )
        sys.stdout.write(
                'STATUS: Crisis handled, system stable\n'
            )
    except PermissionError:
        print(
        f"\nCRISIS ALERT: Attempting access to'{file_name}'..."
    )
        sys.stderr.write(
            'RESPONSE: Security protocols deny access\n'
            )
        sys.stdout.write(
                'STATUS: Crisis handled, security maintained\n'
            )
    except Exception:
        print(
        f"\nCRISIS ALERT: Attempting access to'{file_name}'..."
    )
        sys.stderr.write(
            'Something went wrong, try again...\n'
            )


def main() -> None:
    print(
        '=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n'
    )

    print(
        "CRISIS ALERT: Attempting access to'lost_archive.txt'..."
    )

    crisis_handler('lost_archive.txt')
    crisis_handler('classified_vault.txt')
    crisis_handler('standard_archive.txt')

    print(
        '\nAll crisis scenarios handled successfully. Archives secure.'
    )


if __name__ == "__main__":
    main()