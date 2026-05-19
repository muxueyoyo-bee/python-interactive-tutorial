try:
    result = int('not a number')
    except (AttributeError, TypeError) as e:
        print(f'Caught (AttributeError, TypeError): {e}')
    except (ImportError, AttributeError) as e:
        print(f'Caught (ImportError, AttributeError): {e}')
    except (NetrcParseError, OSError) as e:
        print(f'Caught (NetrcParseError, OSError): {e}')
finally:
    print('Cleanup complete')