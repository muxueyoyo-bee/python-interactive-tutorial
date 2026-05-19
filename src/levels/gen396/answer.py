try:
    result = int('not a number')
    except FileExistsError as e:
        print(f'Caught FileExistsError: {e}')
finally:
    print('Cleanup complete')