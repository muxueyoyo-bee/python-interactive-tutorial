try:
    result = int('not a number')
    except NameError as e:
        print(f'Caught NameError: {e}')
finally:
    print('Cleanup complete')