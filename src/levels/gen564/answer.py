try:
    result = int('not a number')
    except Exception as e:
        print(f'Caught Exception: {e}')
    except StopIteration as e:
        print(f'Caught StopIteration: {e}')
finally:
    print('Cleanup complete')