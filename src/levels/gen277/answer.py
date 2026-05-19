try:
    result = int('not a number')
    except (ValueError, TypeError) as e:
        print(f'Caught (ValueError, TypeError): {e}')
    except (ValueError, TypeError, ValidationError) as e:
        print(f'Caught (ValueError, TypeError, ValidationError): {e}')
    except AttributeError as e:
        print(f'Caught AttributeError: {e}')
finally:
    print('Cleanup complete')