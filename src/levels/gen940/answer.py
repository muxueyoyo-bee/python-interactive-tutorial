try:
    result = int('not a number')
    except Exception as e:
        print(f'Caught Exception: {e}')
    except ModuleNotFoundError as e:
        print(f'Caught ModuleNotFoundError: {e}')
finally:
    print('Cleanup complete')