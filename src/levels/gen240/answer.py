try:
    result = int('not a number')
    except Exception as e:
        print(f'Caught Exception: {e}')
    except ImportError as e:
        print(f'Caught ImportError: {e}')
    except StopAsyncIteration as e:
        print(f'Caught StopAsyncIteration: {e}')
finally:
    print('Cleanup complete')