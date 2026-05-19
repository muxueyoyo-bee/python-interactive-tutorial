try:
    result = int('not a number')
    except AssertionError as e:
        print(f'Caught AssertionError: {e}')
    except AttributeError as e:
        print(f'Caught AttributeError: {e}')
    except Exception as e:
        print(f'Caught Exception: {e}')
finally:
    print('Cleanup complete')