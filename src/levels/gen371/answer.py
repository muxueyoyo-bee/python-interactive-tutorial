try:
    result = int('not a number')
    except UnicodeDecodeError as e:
        print(f'Caught UnicodeDecodeError: {e}')
    except ValueError as e:
        print(f'Caught ValueError: {e}')
finally:
    print('Cleanup complete')