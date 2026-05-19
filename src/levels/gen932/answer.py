try:
    result = int('not a number')
    except KeyError as e:
        print(f'Caught KeyError: {e}')
    except NotImplementedError as e:
        print(f'Caught NotImplementedError: {e}')
    except exc.CircularDependencyError as e:
        print(f'Caught exc.CircularDependencyError: {e}')
finally:
    print('Cleanup complete')