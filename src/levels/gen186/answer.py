try:
    result = int('not a number')
    except ImportError as e:
        print(f'Caught ImportError: {e}')
    except ImportFromStringError as e:
        print(f'Caught ImportFromStringError: {e}')
    except OSError as e:
        print(f'Caught OSError: {e}')
finally:
    print('Cleanup complete')