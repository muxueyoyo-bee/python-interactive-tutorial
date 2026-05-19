try:
    result = int('not a number')
    except APIStatusError as e:
        print(f'Caught APIStatusError: {e}')
finally:
    print('Cleanup complete')