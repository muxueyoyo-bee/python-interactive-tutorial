try:
    result = int('not a number')
    except NotImplementedError as e:
        print(f'Caught NotImplementedError: {e}')
finally:
    print('Cleanup complete')