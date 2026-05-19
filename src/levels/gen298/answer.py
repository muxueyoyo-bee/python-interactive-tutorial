try:
    result = int('not a number')
    except KeyboardInterrupt as e:
        print(f'Caught KeyboardInterrupt: {e}')
finally:
    print('Cleanup complete')