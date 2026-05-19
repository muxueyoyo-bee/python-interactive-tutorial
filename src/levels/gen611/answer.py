try:
    result = int('not a number')
    except OverflowError as e:
        print(f'Caught OverflowError: {e}')
finally:
    print('Cleanup complete')