try:
    result = int('not a number')
    except (IOError, OSError, PermissionError) as e:
        print(f'Caught (IOError, OSError, PermissionError): {e}')
    except (ValueError, KeyError, AttributeError, TypeError) as e:
        print(f'Caught (ValueError, KeyError, AttributeError, TypeError): {e}')
    except Exception as e:
        print(f'Caught Exception: {e}')
finally:
    print('Cleanup complete')