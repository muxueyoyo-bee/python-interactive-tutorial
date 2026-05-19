try:
    result = int('not a number')
    except EOFError as e:
        print(f'Caught EOFError: {e}')
    except Exception as e:
        print(f'Caught Exception: {e}')
    except IOError as e:
        print(f'Caught IOError: {e}')
finally:
    print('Cleanup complete')