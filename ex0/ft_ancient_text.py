def main() -> None:
    print(
        '=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n'
        )

    print('Accessing Storage Vault: ancient_fragment.txt')
    try:
        f = open("ancient_fragment.txt", "r")
        print('Connection established\n')
    except FileNotFoundError:
        print(
            'ERROR: Storage vault not found. Run data generator first'
              )
        return

    content = f.read()
    print('RECOVERED DATA:')
    print(content)

    f.close()

    print('\nData recovery complete. Storage unit disconnected.')


if __name__ == "__main__":
    main()
