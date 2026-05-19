try:
    result = int('not a number')
    except KeyError as e:
        print(f'Caught KeyError: {e}')
    except StopIteration as e:
        print(f'Caught StopIteration: {e}')
finally:
    print('Cleanup complete')