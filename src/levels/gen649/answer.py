try:
    result = int('not a number')
    except UnicodeEncodeError as e:
        print(f'Caught UnicodeEncodeError: {e}')
finally:
    print('Cleanup complete')