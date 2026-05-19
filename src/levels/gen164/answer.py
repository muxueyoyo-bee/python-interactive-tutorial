try:
    result = int('not a number')
    except IndexError as e:
        print(f'Caught IndexError: {e}')
finally:
    print('Cleanup complete')