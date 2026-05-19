try:
    result = int('not a number')
    except OSError as e:
        print(f'Caught OSError: {e}')
    except StopIteration as e:
        print(f'Caught StopIteration: {e}')
    except TypeError as e:
        print(f'Caught TypeError: {e}')
finally:
    print('Cleanup complete')