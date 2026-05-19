try:
    result = int('not a number')
    except (OSError, IOError) as e:
        print(f'Caught (OSError, IOError): {e}')
    except (json.JSONDecodeError, IOError) as e:
        print(f'Caught (json.JSONDecodeError, IOError): {e}')
    except Exception as e:
        print(f'Caught Exception: {e}')
finally:
    print('Cleanup complete')