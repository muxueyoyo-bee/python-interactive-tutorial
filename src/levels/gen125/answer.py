try:
    result = int('not a number')
    except OSError as e:
        print(f'Caught OSError: {e}')
    except OverflowError as e:
        print(f'Caught OverflowError: {e}')
    except ValueError as e:
        print(f'Caught ValueError: {e}')
finally:
    print('Cleanup complete')