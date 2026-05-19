try:
    result = int('not a number')
    except configparser.NoSectionError as e:
        print(f'Caught configparser.NoSectionError: {e}')
finally:
    print('Cleanup complete')