try:
    result = int('not a number')
    except IndexError as e:
        print(f'Caught IndexError: {e}')
    except UnicodeDecodeError as e:
        print(f'Caught UnicodeDecodeError: {e}')
finally:
    print('Cleanup complete')