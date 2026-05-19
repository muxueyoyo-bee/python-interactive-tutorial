try:
    result = int('not a number')
    except PropertyNotFoundError as e:
        print(f'Caught PropertyNotFoundError: {e}')
finally:
    print('Cleanup complete')