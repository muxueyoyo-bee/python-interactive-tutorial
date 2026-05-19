try:
    result = int('not a number')
    except (IndexError, TypeError, ValueError) as e:
        print(f'Caught (IndexError, TypeError, ValueError): {e}')
    except (KeyError, IndexError, AttributeError) as e:
        print(f'Caught (KeyError, IndexError, AttributeError): {e}')
    except (ValueError, LookupError) as e:
        print(f'Caught (ValueError, LookupError): {e}')
finally:
    print('Cleanup complete')