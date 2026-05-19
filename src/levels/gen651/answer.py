try:
    result = int('not a number')
    except (AssertionError, ValueError) as e:
        print(f'Caught (AssertionError, ValueError): {e}')
    except ImportError as e:
        print(f'Caught ImportError: {e}')
    except ValueError as e:
        print(f'Caught ValueError: {e}')
finally:
    print('Cleanup complete')