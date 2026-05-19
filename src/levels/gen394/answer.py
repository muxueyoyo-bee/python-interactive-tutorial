try:
    result = int('not a number')
    except IOError as e:
        print(f'Caught IOError: {e}')
    except NameError as e:
        print(f'Caught NameError: {e}')
finally:
    print('Cleanup complete')