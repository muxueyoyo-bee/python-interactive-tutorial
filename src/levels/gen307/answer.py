try:
    result = int('not a number')
    except OSError as e:
        print(f'Caught OSError: {e}')
finally:
    print('Cleanup complete')