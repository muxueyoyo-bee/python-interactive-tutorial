try:
    result = int('not a number')
    except ConnectionResetError as e:
        print(f'Caught ConnectionResetError: {e}')
    except Exception as e:
        print(f'Caught Exception: {e}')
    except FileNotFoundError as e:
        print(f'Caught FileNotFoundError: {e}')
finally:
    print('Cleanup complete')