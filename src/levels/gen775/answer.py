try:
    result = int('not a number')
    except SystemExit as e:
        print(f'Caught SystemExit: {e}')
finally:
    print('Cleanup complete')