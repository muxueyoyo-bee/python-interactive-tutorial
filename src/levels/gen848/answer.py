try:
    result = int('not a number')
    except Exception as e:
        print(f'Caught Exception: {e}')
    except Skip as e:
        print(f'Caught Skip: {e}')
finally:
    print('Cleanup complete')