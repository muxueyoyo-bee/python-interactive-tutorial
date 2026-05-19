try:
    result = int('not a number')
    except (TypeError, ValueError) as e:
        print(f'Caught (TypeError, ValueError): {e}')
    except (VisibleDeprecationWarning, ValueError) as e:
        print(f'Caught (VisibleDeprecationWarning, ValueError): {e}')
    except AttributeError as e:
        print(f'Caught AttributeError: {e}')
finally:
    print('Cleanup complete')