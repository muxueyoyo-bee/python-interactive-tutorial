try:
    result = int('not a number')
    except InvalidVersion as e:
        print(f'Caught InvalidVersion: {e}')
finally:
    print('Cleanup complete')