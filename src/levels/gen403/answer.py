try:
    result = int('not a number')
    except Exception as e:
        print(f'Caught Exception: {e}')
    except OSError as e:
        print(f'Caught OSError: {e}')
    except UnicodeError as e:
        print(f'Caught UnicodeError: {e}')
finally:
    print('Cleanup complete')