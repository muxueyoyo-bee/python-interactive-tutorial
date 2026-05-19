try:
    result = int('not a number')
    except PermissionError as e:
        print(f'Caught PermissionError: {e}')
finally:
    print('Cleanup complete')