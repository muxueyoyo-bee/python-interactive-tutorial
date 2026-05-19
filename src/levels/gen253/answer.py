try:
    result = int('not a number')
    except AttributeError as e:
        print(f'Caught AttributeError: {e}')
    except DiffError as e:
        print(f'Caught DiffError: {e}')
    except EnvironmentError as e:
        print(f'Caught EnvironmentError: {e}')
finally:
    print('Cleanup complete')