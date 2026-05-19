try:
    result = int('not a number')
    except Exception as e:
        print(f'Caught Exception: {e}')
    except StopAsyncIteration as e:
        print(f'Caught StopAsyncIteration: {e}')
    except self._terminate_handled_exceptions() as e:
        print(f'Caught self._terminate_handled_exceptions(): {e}')
finally:
    print('Cleanup complete')