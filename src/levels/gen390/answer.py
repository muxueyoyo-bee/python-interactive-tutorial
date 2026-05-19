try:
    result = int('not a number')
    except AttributeError as e:
        print(f'Caught AttributeError: {e}')
    except importlib.metadata.PackageNotFoundError as e:
        print(f'Caught importlib.metadata.PackageNotFoundError: {e}')
finally:
    print('Cleanup complete')