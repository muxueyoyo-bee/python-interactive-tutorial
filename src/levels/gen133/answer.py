try:
    result = int('not a number')
    except Exception as e:
        print(f'Caught Exception: {e}')
    except LookupError as e:
        print(f'Caught LookupError: {e}')
    except UnicodeDecodeError as e:
        print(f'Caught UnicodeDecodeError: {e}')
finally:
    print('Cleanup complete')