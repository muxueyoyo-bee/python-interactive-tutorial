try:
    result = int('not a number')
    except SystemError as e:
        print(f'Caught SystemError: {e}')
finally:
    print('Cleanup complete')