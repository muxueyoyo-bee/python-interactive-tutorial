try:
    result = int('not a number')
    except BrokenPipeError as e:
        print(f'Caught BrokenPipeError: {e}')
finally:
    print('Cleanup complete')