try:
    result = int('not a number')
    except (AttributeError, NameError) as e:
        print(f'Caught (AttributeError, NameError): {e}')
    except (TypeError, NotImplementedError) as e:
        print(f'Caught (TypeError, NotImplementedError): {e}')
    except (TypeError, ValueError) as e:
        print(f'Caught (TypeError, ValueError): {e}')
finally:
    print('Cleanup complete')