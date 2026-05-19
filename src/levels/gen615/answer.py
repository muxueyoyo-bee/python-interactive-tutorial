try:
    result = int('not a number')
    except (AttributeError, TypeError) as e:
        print(f'Caught (AttributeError, TypeError): {e}')
    except (KeyError, ValueError, IndexError) as e:
        print(f'Caught (KeyError, ValueError, IndexError): {e}')
    except AttributeError as e:
        print(f'Caught AttributeError: {e}')
finally:
    print('Cleanup complete')