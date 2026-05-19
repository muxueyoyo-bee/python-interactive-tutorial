try:
    result = int('not a number')
    except (AttributeError, KeyError) as e:
        print(f'Caught (AttributeError, KeyError): {e}')
    except (AttributeError, TypeError) as e:
        print(f'Caught (AttributeError, TypeError): {e}')
    except AttributeError as e:
        print(f'Caught AttributeError: {e}')
finally:
    print('Cleanup complete')