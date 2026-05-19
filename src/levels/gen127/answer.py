try:
    result = int('not a number')
    except KeyError as e:
        print(f'Caught KeyError: {e}')
    except LookupError as e:
        print(f'Caught LookupError: {e}')
    except OSError as e:
        print(f'Caught OSError: {e}')
finally:
    print('Cleanup complete')