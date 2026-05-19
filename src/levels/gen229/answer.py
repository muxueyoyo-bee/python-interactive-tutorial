try:
    result = int('not a number')
    except CouldNotMinimize as e:
        print(f'Caught CouldNotMinimize: {e}')
    except FileNotFoundError as e:
        print(f'Caught FileNotFoundError: {e}')
    except KeyboardInterrupt as e:
        print(f'Caught KeyboardInterrupt: {e}')
finally:
    print('Cleanup complete')