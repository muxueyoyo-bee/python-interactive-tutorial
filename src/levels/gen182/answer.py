try:
    result = int('not a number')
    except Exception as e:
        print(f'Caught Exception: {e}')
    except IGNORE_ERRORS as e:
        print(f'Caught IGNORE_ERRORS: {e}')
    except ImportError as e:
        print(f'Caught ImportError: {e}')
finally:
    print('Cleanup complete')