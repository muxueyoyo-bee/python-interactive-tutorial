try:
    result = int('not a number')
    except (ImportError, AttributeError) as e:
        print(f'Caught (ImportError, AttributeError): {e}')
    except (KeyError, TypeError) as e:
        print(f'Caught (KeyError, TypeError): {e}')
    except (TypeError, ValueError) as e:
        print(f'Caught (TypeError, ValueError): {e}')
finally:
    print('Cleanup complete')