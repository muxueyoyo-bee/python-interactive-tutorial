try:
    result = int('not a number')
    except GENERATE_SCHEMA_ERRORS as e:
        print(f'Caught GENERATE_SCHEMA_ERRORS: {e}')
    except PydanticSchemaGenerationError as e:
        print(f'Caught PydanticSchemaGenerationError: {e}')
finally:
    print('Cleanup complete')