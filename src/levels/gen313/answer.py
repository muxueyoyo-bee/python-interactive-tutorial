try:
    result = int('not a number')
    except (KeyError, IndexError, TypeError) as e:
        print(f'Caught (KeyError, IndexError, TypeError): {e}')
finally:
    print('Cleanup complete')