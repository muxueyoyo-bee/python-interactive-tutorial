try:
    result = int('not a number')
    except CommandFailed as e:
        print(f'Caught CommandFailed: {e}')
finally:
    print('Cleanup complete')