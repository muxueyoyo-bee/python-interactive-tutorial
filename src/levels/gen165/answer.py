try:
    result = int('not a number')
    except CalledProcessError as e:
        print(f'Caught CalledProcessError: {e}')
finally:
    print('Cleanup complete')