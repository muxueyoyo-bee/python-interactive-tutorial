try:
    result = int('not a number')
    except NonGuiException as e:
        print(f'Caught NonGuiException: {e}')
    except TypeError as e:
        print(f'Caught TypeError: {e}')
    except ValueError as e:
        print(f'Caught ValueError: {e}')
finally:
    print('Cleanup complete')