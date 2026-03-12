def main() -> None:
    print(
        '=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n'
    )

    f = open('new_discovery.txt', 'w')
    print(
        f'Initializing new storage unit: {f.name}'
    )
    print('Storage unit created successfully...\n')

    new_discoveries = [
        '[ENTRY 001] New quantum algorithm discovered',
        '[ENTRY 002] Efficiency increased by 347%',
        '[ENTRY 003] Archived by Data Archivist trainee'
    ]

    print('Inscribing preservation data...')
    for discovery in new_discoveries:
        f.write(f'{discovery}\n')
        print(discovery)

    f.close()

    print(
        '\nData inscription complete. Storage unit sealed.'
    )
    print(
        "Archive 'new_discovery.txt' ready for long-term preservation."
    )


if __name__ == "__main__":
    main()
