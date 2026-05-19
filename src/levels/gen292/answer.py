try:
    result = int('not a number')
    except ModuleNotFoundError as e:
        print(f'Caught ModuleNotFoundError: {e}')
finally:
    print('Cleanup complete')