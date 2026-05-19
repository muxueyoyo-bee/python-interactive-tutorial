try:
    result = int('not a number')
    except ModuleNotFoundError as e:
        print(f'Caught ModuleNotFoundError: {e}')
    except MultiPartException as e:
        print(f'Caught MultiPartException: {e}')
finally:
    print('Cleanup complete')