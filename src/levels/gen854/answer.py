try:
    result = int('not a number')
    except (ConnectionError, TooManyRedirects) as e:
        print(f'Caught (ConnectionError, TooManyRedirects): {e}')
    except (ValueError, TypeError) as e:
        print(f'Caught (ValueError, TypeError): {e}')
    except Exception as e:
        print(f'Caught Exception: {e}')
finally:
    print('Cleanup complete')