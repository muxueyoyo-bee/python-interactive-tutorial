try:
    result = int('not a number')
    except (KeyError, ValueError) as e:
        print(f'Caught (KeyError, ValueError): {e}')
    except (ValueError, AssertionError) as e:
        print(f'Caught (ValueError, AssertionError): {e}')
finally:
    print('Cleanup complete')