try:
    result = int('not a number')
    except (KeyError, TypeError, InvalidIndexError) as e:
        print(f'Caught (KeyError, TypeError, InvalidIndexError): {e}')
    except (TypeError, ValueError, LossySetitemError) as e:
        print(f'Caught (TypeError, ValueError, LossySetitemError): {e}')
    except Exception as e:
        print(f'Caught Exception: {e}')
finally:
    print('Cleanup complete')