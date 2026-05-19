try:
    result = int('not a number')
    except (json.JSONDecodeError, OSError) as e:
        print(f'Caught (json.JSONDecodeError, OSError): {e}')
    except ValueError as e:
        print(f'Caught ValueError: {e}')
    except json.JSONDecodeError as e:
        print(f'Caught json.JSONDecodeError: {e}')
finally:
    print('Cleanup complete')