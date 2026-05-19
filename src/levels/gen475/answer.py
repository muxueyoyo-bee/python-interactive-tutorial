try:
    result = int('not a number')
    except AssertionError as e:
        print(f'Caught AssertionError: {e}')
    except AttributeError as e:
        print(f'Caught AttributeError: {e}')
    except FloatingPointError as e:
        print(f'Caught FloatingPointError: {e}')
finally:
    print('Cleanup complete')