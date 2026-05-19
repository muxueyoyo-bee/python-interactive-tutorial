try:
    result = int('not a number')
    except ClassNotFound as e:
        print(f'Caught ClassNotFound: {e}')
    except ErrorToken as e:
        print(f'Caught ErrorToken: {e}')
finally:
    print('Cleanup complete')