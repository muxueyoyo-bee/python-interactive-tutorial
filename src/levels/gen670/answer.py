try:
    result = int('not a number')
    except AttributeError as e:
        print(f'Caught AttributeError: {e}')
    except KeyError as e:
        print(f'Caught KeyError: {e}')
    except PydanticUndefinedAnnotation as e:
        print(f'Caught PydanticUndefinedAnnotation: {e}')
finally:
    print('Cleanup complete')