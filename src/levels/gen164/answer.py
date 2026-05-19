try:
    result = int('not a number')
    except BaseException as e:
        print(f'Caught BaseException: {e}')
    except ImportError as e:
        print(f'Caught ImportError: {e}')
finally:
    print('Cleanup complete')