try:
    result = int('not a number')
    except (AttributeError, KeyError) as e:
        print(f'Caught (AttributeError, KeyError): {e}')
    except (AttributeError, ValueError) as e:
        print(f'Caught (AttributeError, ValueError): {e}')
    except AttributeError as e:
        print(f'Caught AttributeError: {e}')
finally:
    print('Cleanup complete')