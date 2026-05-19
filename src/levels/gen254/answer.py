try:
    result = int('not a number')
    except ImportError as e:
        print(f'Caught ImportError: {e}')
    except SoftTimeLimitExceeded as e:
        print(f'Caught SoftTimeLimitExceeded: {e}')
finally:
    print('Cleanup complete')