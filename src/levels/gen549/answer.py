try:
    result = int('not a number')
    except JSONDecodeError as e:
        print(f'Caught JSONDecodeError: {e}')
    except NotImplementedError as e:
        print(f'Caught NotImplementedError: {e}')
finally:
    print('Cleanup complete')