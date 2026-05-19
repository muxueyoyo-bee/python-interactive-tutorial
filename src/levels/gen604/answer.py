try:
    result = int('not a number')
    except (ValueError, AttributeError, TypeError) as e:
        print(f'Caught (ValueError, AttributeError, TypeError): {e}')
    except Exception as e:
        print(f'Caught Exception: {e}')
    except TypeError as e:
        print(f'Caught TypeError: {e}')
finally:
    print('Cleanup complete')