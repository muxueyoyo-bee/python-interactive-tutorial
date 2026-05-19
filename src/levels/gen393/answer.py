try:
    result = int('not a number')
    except (AttributeError, IndexError) as e:
        print(f'Caught (AttributeError, IndexError): {e}')
finally:
    print('Cleanup complete')