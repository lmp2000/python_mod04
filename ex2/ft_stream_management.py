import sys


def main() -> None:
    print(
        '=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n'
    )

    archivist_id = input(
        'Input Stream Active. Enter archives ID: '
    )
    status = input(
        'Input Stream Active. Enter status report: '
    )

    sys.stdout.write(
        f'\n[STANDARD] Archive status from {archivist_id}: {status}\n'
        )
    sys.stderr.write(
        '[ALERT] System diagnostic: Communication channels verified\n'
    )
    sys.stdout.write(
        '[STANDARD] Data transmission complete\n'
    )

    print(
        '\nThree-channel communication test successful.'
    )


if __name__ == "__main__":
    main()