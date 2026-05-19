try:
    result = int('not a number')
    except EnvCommandError as e:
        print(f'Caught EnvCommandError: {e}')
    except Exception as e:
        print(f'Caught Exception: {e}')
    except KeyboardInterrupt as e:
        print(f'Caught KeyboardInterrupt: {e}')
finally:
    print('Cleanup complete')