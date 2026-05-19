try:
    result = int('not a number')
    except ImportError as e:
        print(f'Caught ImportError: {e}')
    except brotli.error as e:
        print(f'Caught brotli.error: {e}')
    except zlib.error as e:
        print(f'Caught zlib.error: {e}')
finally:
    print('Cleanup complete')