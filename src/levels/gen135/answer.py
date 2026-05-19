try:
    result = int('not a number')
    except (AttributeError, OSError) as e:
        print(f'Caught (AttributeError, OSError): {e}')
    except (OSError, AttributeError) as e:
        print(f'Caught (OSError, AttributeError): {e}')
    except StopAsyncIteration as e:
        print(f'Caught StopAsyncIteration: {e}')
finally:
    print('Cleanup complete')