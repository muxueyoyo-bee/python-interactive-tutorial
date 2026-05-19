try:
    result = int('not a number')
    except FileNotFoundError as e:
        print(f'Caught FileNotFoundError: {e}')
finally:
    print('Cleanup complete')