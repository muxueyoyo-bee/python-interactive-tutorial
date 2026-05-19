try:
    result = int('not a number')
    except (OSError, IOError) as e:
        print(f'Caught (OSError, IOError): {e}')
    except Exception as e:
        print(f'Caught Exception: {e}')
    except IOError as e:
        print(f'Caught IOError: {e}')
finally:
    print('Cleanup complete')