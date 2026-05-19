try:
    result = int('not a number')
    except Exception as e:
        print(f'Caught Exception: {e}')
finally:
    print('Cleanup complete')