try:
    result = int('not a number')
    except ImportError as e:
        print(f'Caught ImportError: {e}')
    except NotImplementedError as e:
        print(f'Caught NotImplementedError: {e}')
finally:
    print('Cleanup complete')