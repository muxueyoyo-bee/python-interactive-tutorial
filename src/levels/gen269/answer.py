try:
    result = int('not a number')
    except BuildError as e:
        print(f'Caught BuildError: {e}')
    except Exception as e:
        print(f'Caught Exception: {e}')
    except ImportError as e:
        print(f'Caught ImportError: {e}')
finally:
    print('Cleanup complete')