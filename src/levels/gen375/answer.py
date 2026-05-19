try:
    result = int('not a number')
    except PydanticSchemaGenerationError as e:
        print(f'Caught PydanticSchemaGenerationError: {e}')
finally:
    print('Cleanup complete')