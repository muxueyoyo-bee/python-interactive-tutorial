try:
    result = int('not a number')
    except (EOFError, ValueError, TypeError) as e:
        print(f'Caught (EOFError, ValueError, TypeError): {e}')
    except (FileNotFoundError, IsADirectoryError, PermissionError) as e:
        print(f'Caught (FileNotFoundError, IsADirectoryError, PermissionError): {e}')
    except BaseException as e:
        print(f'Caught BaseException: {e}')
finally:
    print('Cleanup complete')