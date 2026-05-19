try:
    result = int('not a number')
    except NotImplementedError as e:
        print(f'Caught NotImplementedError: {e}')
    except OSError as e:
        print(f'Caught OSError: {e}')
finally:
    print('Cleanup complete')