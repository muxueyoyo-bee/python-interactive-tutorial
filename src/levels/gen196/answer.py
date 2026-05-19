try:
    result = int('not a number')
    except IndexError as e:
        print(f'Caught IndexError: {e}')
    except SystemExit as e:
        print(f'Caught SystemExit: {e}')
finally:
    print('Cleanup complete')