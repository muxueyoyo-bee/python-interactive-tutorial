try:
    result = int('not a number')
    except EOFError as e:
        print(f'Caught EOFError: {e}')
    except KeyError as e:
        print(f'Caught KeyError: {e}')
finally:
    print('Cleanup complete')