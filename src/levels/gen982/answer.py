try:
    result = int('not a number')
    except network_exceptions as e:
        print(f'Caught network_exceptions: {e}')
finally:
    print('Cleanup complete')