try:
    result = int('not a number')
    except BuildError as e:
        print(f'Caught BuildError: {e}')
finally:
    print('Cleanup complete')