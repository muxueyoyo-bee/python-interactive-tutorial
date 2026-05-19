try:
    result = int('not a number')
    except IndexError as e:
        print(f'Caught IndexError: {e}')
    except ValueError as e:
        print(f'Caught ValueError: {e}')
finally:
    print('Cleanup complete')