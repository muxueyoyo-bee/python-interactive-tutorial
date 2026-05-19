try:
    result = int('not a number')
    except Exception as e:
        print(f'Caught Exception: {e}')
    except JS_Break as e:
        print(f'Caught JS_Break: {e}')
    except JS_Continue as e:
        print(f'Caught JS_Continue: {e}')
finally:
    print('Cleanup complete')