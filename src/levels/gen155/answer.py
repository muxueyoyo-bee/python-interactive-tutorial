try:
    result = int('not a number')
    except (ProcessLookupError, ValueError) as e:
        print(f'Caught (ProcessLookupError, ValueError): {e}')
    except (json.JSONDecodeError, OSError) as e:
        print(f'Caught (json.JSONDecodeError, OSError): {e}')
    except (json.JSONDecodeError, OSError, KeyError) as e:
        print(f'Caught (json.JSONDecodeError, OSError, KeyError): {e}')
finally:
    print('Cleanup complete')