try:
    result = int('not a number')
    except (jsonschema.ValidationError, jsonschema.exceptions.SchemaError) as e:
        print(f'Caught (jsonschema.ValidationError, jsonschema.exceptions.SchemaError): {e}')
    except Exception as e:
        print(f'Caught Exception: {e}')
    except ImportError as e:
        print(f'Caught ImportError: {e}')
finally:
    print('Cleanup complete')