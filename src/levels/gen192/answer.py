try:
    result = int('not a number')
    except URLError as e:
        print(f'Caught URLError: {e}')
finally:
    print('Cleanup complete')