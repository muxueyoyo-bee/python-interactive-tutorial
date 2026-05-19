try:
    result = int('not a number')
    except (OSError, TypeError) as e:
        print(f'Caught (OSError, TypeError): {e}')
    except (ValueError, OverflowError) as e:
        print(f'Caught (ValueError, OverflowError): {e}')
    except AttributeError as e:
        print(f'Caught AttributeError: {e}')
finally:
    print('Cleanup complete')