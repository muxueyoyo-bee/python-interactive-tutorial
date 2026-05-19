try:
    result = int('not a number')
    except AttributeError as e:
        print(f'Caught AttributeError: {e}')
    except ModuleNotFoundError as e:
        print(f'Caught ModuleNotFoundError: {e}')
finally:
    print('Cleanup complete')