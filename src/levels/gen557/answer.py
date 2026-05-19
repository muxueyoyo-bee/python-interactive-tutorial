try:
    result = int('not a number')
    except CleoCommandNotFoundError as e:
        print(f'Caught CleoCommandNotFoundError: {e}')
    except CleoError as e:
        print(f'Caught CleoError: {e}')
    except PoetryRuntimeError as e:
        print(f'Caught PoetryRuntimeError: {e}')
finally:
    print('Cleanup complete')