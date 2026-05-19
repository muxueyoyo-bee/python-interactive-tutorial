try:
    result = int('not a number')
    except (AttributeError, KeyError) as e:
        print(f'Caught (AttributeError, KeyError): {e}')
    except (ValueError, TypeError) as e:
        print(f'Caught (ValueError, TypeError): {e}')
    except IndexError as e:
        print(f'Caught IndexError: {e}')
finally:
    print('Cleanup complete')