try:
    result = int('not a number')
    except KeyError as e:
        print(f'Caught KeyError: {e}')
    except ResolutionError as e:
        print(f'Caught ResolutionError: {e}')
    except ValueError as e:
        print(f'Caught ValueError: {e}')
finally:
    print('Cleanup complete')