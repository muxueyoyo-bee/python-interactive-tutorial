try:
    result = int('not a number')
    except BrokenPipeError as e:
        print(f'Caught BrokenPipeError: {e}')
    except Exception as e:
        print(f'Caught Exception: {e}')
    except KeyboardInterrupt as e:
        print(f'Caught KeyboardInterrupt: {e}')
finally:
    print('Cleanup complete')