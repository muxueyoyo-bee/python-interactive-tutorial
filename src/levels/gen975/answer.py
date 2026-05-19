try:
    result = int('not a number')
    except OSError as e:
        print(f'Caught OSError: {e}')
    except network_exceptions as e:
        print(f'Caught network_exceptions: {e}')
finally:
    print('Cleanup complete')