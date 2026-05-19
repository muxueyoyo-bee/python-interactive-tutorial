try:
    result = int('not a number')
    except FileNotFoundError as e:
        print(f'Caught FileNotFoundError: {e}')
    except MalformedRangeHeader as e:
        print(f'Caught MalformedRangeHeader: {e}')
    except OSError as e:
        print(f'Caught OSError: {e}')
finally:
    print('Cleanup complete')