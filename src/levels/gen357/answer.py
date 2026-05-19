try:
    result = int('not a number')
    except BaseException as e:
        print(f'Caught BaseException: {e}')
finally:
    print('Cleanup complete')