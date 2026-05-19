try:
    result = int('not a number')
    except Exception as e:
        print(f'Caught Exception: {e}')
    except ValueError as e:
        print(f'Caught ValueError: {e}')
finally:
    print('Cleanup complete')