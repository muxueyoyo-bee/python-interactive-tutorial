try:
    result = int('not a number')
    except StopIteration as e:
        print(f'Caught StopIteration: {e}')
finally:
    print('Cleanup complete')