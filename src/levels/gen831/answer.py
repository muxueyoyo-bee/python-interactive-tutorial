try:
    result = int('not a number')
    except ConfigError as e:
        print(f'Caught ConfigError: {e}')
    except Exception as e:
        print(f'Caught Exception: {e}')
    except SyntaxError as e:
        print(f'Caught SyntaxError: {e}')
finally:
    print('Cleanup complete')