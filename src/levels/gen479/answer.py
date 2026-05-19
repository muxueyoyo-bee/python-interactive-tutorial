try:
    result = int('not a number')
    except DeprecationWarning as e:
        print(f'Caught DeprecationWarning: {e}')
    except Exception as e:
        print(f'Caught Exception: {e}')
    except TypeError as e:
        print(f'Caught TypeError: {e}')
finally:
    print('Cleanup complete')