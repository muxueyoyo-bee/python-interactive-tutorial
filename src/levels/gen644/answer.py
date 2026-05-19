try:
    result = int('not a number')
    except (ChunkedEncodingError, ContentDecodingError, RuntimeError) as e:
        print(f'Caught (ChunkedEncodingError, ContentDecodingError, RuntimeError): {e}')
    except KeyError as e:
        print(f'Caught KeyError: {e}')
    except StopIteration as e:
        print(f'Caught StopIteration: {e}')
finally:
    print('Cleanup complete')