try:
    result = int('not a number')
    except UnicodeDecodeError as e:
        print(f'Caught UnicodeDecodeError: {e}')
    except shellingham.ShellDetectionFailure as e:
        print(f'Caught shellingham.ShellDetectionFailure: {e}')
finally:
    print('Cleanup complete')