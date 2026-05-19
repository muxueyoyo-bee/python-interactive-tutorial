try:
    result = int('not a number')
    except (KeyError, AssertionError) as e:
        print(f'Caught (KeyError, AssertionError): {e}')
    except Exception as e:
        print(f'Caught Exception: {e}')
    except KeyError as e:
        print(f'Caught KeyError: {e}')
finally:
    print('Cleanup complete')