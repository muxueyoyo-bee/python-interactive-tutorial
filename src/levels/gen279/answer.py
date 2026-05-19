try:
    result = int('not a number')
    except RuntimeError as e:
        print(f'Caught RuntimeError: {e}')
finally:
    print('Cleanup complete')