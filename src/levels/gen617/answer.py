try:
    result = int('not a number')
    except (TypeError, InvalidIndexError) as e:
        print(f'Caught (TypeError, InvalidIndexError): {e}')
    except (ValueError, TypeError) as e:
        print(f'Caught (ValueError, TypeError): {e}')
    except (ValueError, TypeError, LossySetitemError) as e:
        print(f'Caught (ValueError, TypeError, LossySetitemError): {e}')
finally:
    print('Cleanup complete')