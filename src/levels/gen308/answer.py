try:
    result = int('not a number')
    except (AttributeError, OSError) as e:
        print(f'Caught (AttributeError, OSError): {e}')
    except Exception as e:
        print(f'Caught Exception: {e}')
finally:
    print('Cleanup complete')