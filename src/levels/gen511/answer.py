try:
    result = int('not a number')
    except ForbiddenQualifier as e:
        print(f'Caught ForbiddenQualifier: {e}')
    except KeyError as e:
        print(f'Caught KeyError: {e}')
finally:
    print('Cleanup complete')