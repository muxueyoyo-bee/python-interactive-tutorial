try:
    result = int('not a number')
    except CompileError as e:
        print(f'Caught CompileError: {e}')
finally:
    print('Cleanup complete')