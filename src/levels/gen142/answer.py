try:
    result = int('not a number')
    except IOError as e:
        print(f'Caught IOError: {e}')
finally:
    print('Cleanup complete')