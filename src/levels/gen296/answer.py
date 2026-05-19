try:
    result = int('not a number')
    except EOFError as e:
        print(f'Caught EOFError: {e}')
    except KeyboardInterrupt as e:
        print(f'Caught KeyboardInterrupt: {e}')
    except OSError as e:
        print(f'Caught OSError: {e}')
finally:
    print('Cleanup complete')