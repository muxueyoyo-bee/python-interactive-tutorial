try:
    result = int('not a number')
    except io.UnsupportedOperation as e:
        print(f'Caught io.UnsupportedOperation: {e}')
finally:
    print('Cleanup complete')