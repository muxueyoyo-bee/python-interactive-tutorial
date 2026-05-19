try:
    result = int('not a number')
    except KeyError as e:
        print(f'Caught KeyError: {e}')
    except NonIntersectingPathException as e:
        print(f'Caught NonIntersectingPathException: {e}')
    except ValueError as e:
        print(f'Caught ValueError: {e}')
finally:
    print('Cleanup complete')