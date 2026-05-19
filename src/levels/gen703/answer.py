try:
    result = int('not a number')
    except zlib.error as e:
        print(f'Caught zlib.error: {e}')
finally:
    print('Cleanup complete')