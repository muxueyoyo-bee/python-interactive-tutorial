try:
    result = int('not a number')
    except BaseException as e:
        print(f'Caught BaseException: {e}')
    except Exception as e:
        print(f'Caught Exception: {e}')
    except LookupError as e:
        print(f'Caught LookupError: {e}')
finally:
    print('Cleanup complete')