try:
    result = int('not a number')
    except JsonSchemaValueException as e:
        print(f'Caught JsonSchemaValueException: {e}')
finally:
    print('Cleanup complete')