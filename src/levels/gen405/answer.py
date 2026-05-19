try:
    result = int('not a number')
    except UnicodeDecodeError as e:
        print(f'Caught UnicodeDecodeError: {e}')
finally:
    print('Cleanup complete')