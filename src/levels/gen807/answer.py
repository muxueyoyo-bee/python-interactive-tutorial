try:
    result = int('not a number')
    except SyntaxError as e:
        print(f'Caught SyntaxError: {e}')
finally:
    print('Cleanup complete')