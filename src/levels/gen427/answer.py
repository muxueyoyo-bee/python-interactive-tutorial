try:
    result = int('not a number')
    except (ImportError, ValueError) as e:
        print(f'Caught (ImportError, ValueError): {e}')
    except TypeError as e:
        print(f'Caught TypeError: {e}')
finally:
    print('Cleanup complete')