try:
    result = int('not a number')
    except (AttributeError, TypeError) as e:
        print(f'Caught (AttributeError, TypeError): {e}')
finally:
    print('Cleanup complete')