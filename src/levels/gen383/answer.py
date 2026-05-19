try:
    result = int('not a number')
    except (ImportError, AssertionError) as e:
        print(f'Caught (ImportError, AssertionError): {e}')
    except AttributeError as e:
        print(f'Caught AttributeError: {e}')
    except ImportError as e:
        print(f'Caught ImportError: {e}')
finally:
    print('Cleanup complete')