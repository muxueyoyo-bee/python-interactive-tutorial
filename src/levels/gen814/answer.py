try:
    result = int('not a number')
    except AttributeError as e:
        print(f'Caught AttributeError: {e}')
    except EOFError as e:
        print(f'Caught EOFError: {e}')
    except Exception as e:
        print(f'Caught Exception: {e}')
finally:
    print('Cleanup complete')