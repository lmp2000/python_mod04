def main() -> None:
    print(
        '=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n'
    )

    print(
        'Initiating secure vault access...'
    )

    try:
        with open('classified_data.txt', 'r') as f:
            content = f.read()
        print(
            'Vault connection established with failsafe protocols\n'
        )
    except FileNotFoundError as e:
        print(e)
        return

    print('SECURE EXTRACTION:')
    print(content)
    print()

    print('SECURE PRESERVATION:')

    with open('new_discovery.txt', 'w') as f:
        f.write(content)
        print(
            '[CLASSIFIED] New security protocols archived'
        )

    if f.closed:
        print(
            'Vault automatically sealed upon completion\n'
            )

    print(
        'All vault operations completed with maximum security.'
    )


if __name__ == "__main__":
    main()
