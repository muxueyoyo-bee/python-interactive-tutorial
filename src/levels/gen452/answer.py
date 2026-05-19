try:
    result = int('not a number')
    except (TypeError, ValueError) as e:
        print(f'Caught (TypeError, ValueError): {e}')
    except (TypeError, ValueError, OverflowError) as e:
        print(f'Caught (TypeError, ValueError, OverflowError): {e}')
    except AttributeError as e:
        print(f'Caught AttributeError: {e}')
finally:
    print('Cleanup complete')