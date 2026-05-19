try:
    result = int('not a number')
    except (KeyError, InvalidIndexError) as e:
        print(f'Caught (KeyError, InvalidIndexError): {e}')
    except (KeyError, TypeError) as e:
        print(f'Caught (KeyError, TypeError): {e}')
    except (KeyError, TypeError, ValueError, LossySetitemError) as e:
        print(f'Caught (KeyError, TypeError, ValueError, LossySetitemError): {e}')
finally:
    print('Cleanup complete')