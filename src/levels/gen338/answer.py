try:
    result = int('not a number')
    except AuthenticationError as e:
        print(f'Caught AuthenticationError: {e}')
finally:
    print('Cleanup complete')