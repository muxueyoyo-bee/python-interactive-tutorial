try:
    result = int('not a number')
    except ImportError as e:
        print(f'Caught ImportError: {e}')
    except ValueError as e:
        print(f'Caught ValueError: {e}')
    except socket.error as e:
        print(f'Caught socket.error: {e}')
finally:
    print('Cleanup complete')