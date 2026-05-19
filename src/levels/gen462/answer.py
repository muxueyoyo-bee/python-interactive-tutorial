try:
    result = int('not a number')
    except RuntimeError as e:
        print(f'Caught RuntimeError: {e}')
    except ValueError as e:
        print(f'Caught ValueError: {e}')
finally:
    print('Cleanup complete')