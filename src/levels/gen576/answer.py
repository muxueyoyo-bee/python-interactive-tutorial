try:
    result = int('not a number')
    except (TypeError, LookupError) as e:
        print(f'Caught (TypeError, LookupError): {e}')
    except AttributeError as e:
        print(f'Caught AttributeError: {e}')
    except Exception as e:
        print(f'Caught Exception: {e}')
finally:
    print('Cleanup complete')