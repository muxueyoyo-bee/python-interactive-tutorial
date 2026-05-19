try:
    result = int('not a number')
    except IndexError as e:
        print(f'Caught IndexError: {e}')
    except LookupError as e:
        print(f'Caught LookupError: {e}')
finally:
    print('Cleanup complete')