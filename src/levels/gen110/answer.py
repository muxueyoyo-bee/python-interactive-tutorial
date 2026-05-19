try:
    result = int('not a number')
    except (AttributeError, NotImplementedError, RuntimeError) as e:
        print(f'Caught (AttributeError, NotImplementedError, RuntimeError): {e}')
finally:
    print('Cleanup complete')