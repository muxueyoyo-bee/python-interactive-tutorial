try:
    result = int('not a number')
    except Exception as e:
        print(f'Caught Exception: {e}')
    except FileNotFoundError as e:
        print(f'Caught FileNotFoundError: {e}')
    except ImportError as e:
        print(f'Caught ImportError: {e}')
finally:
    print('Cleanup complete')