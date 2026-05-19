try:
    result = int('not a number')
    except ExtensionError as e:
        print(f'Caught ExtensionError: {e}')
    except nodes.SkipNode as e:
        print(f'Caught nodes.SkipNode: {e}')
finally:
    print('Cleanup complete')