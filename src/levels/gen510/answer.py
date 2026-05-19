try:
    result = int('not a number')
    except AttributeError as e:
        print(f'Caught AttributeError: {e}')
finally:
    print('Cleanup complete')