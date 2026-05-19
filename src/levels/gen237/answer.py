try:
    result = int('not a number')
    except IOError as e:
        print(f'Caught IOError: {e}')
    except getopt.error as e:
        print(f'Caught getopt.error: {e}')
finally:
    print('Cleanup complete')