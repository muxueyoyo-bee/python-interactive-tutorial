try:
    result = int('not a number')
    except Exception as e:
        print(f'Caught Exception: {e}')
    except SphinxError as e:
        print(f'Caught SphinxError: {e}')
    except allowed_exceptions as e:
        print(f'Caught allowed_exceptions: {e}')
finally:
    print('Cleanup complete')