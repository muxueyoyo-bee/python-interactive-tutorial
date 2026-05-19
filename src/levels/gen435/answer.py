try:
    result = int('not a number')
    except (IOError, OSError) as e:
        print(f'Caught (IOError, OSError): {e}')
    except FileNotFoundError as e:
        print(f'Caught FileNotFoundError: {e}')
    except PermissionError as e:
        print(f'Caught PermissionError: {e}')
finally:
    print('Cleanup complete')