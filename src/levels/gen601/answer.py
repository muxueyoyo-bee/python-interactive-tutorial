try:
    result = int('not a number')
    except (TypeError, decimal.InvalidOperation) as e:
        print(f'Caught (TypeError, decimal.InvalidOperation): {e}')
    except TypeError as e:
        print(f'Caught TypeError: {e}')
finally:
    print('Cleanup complete')