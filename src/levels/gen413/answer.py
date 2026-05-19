try:
    result = int('not a number')
    except ReferenceError as e:
        print(f'Caught ReferenceError: {e}')
finally:
    print('Cleanup complete')