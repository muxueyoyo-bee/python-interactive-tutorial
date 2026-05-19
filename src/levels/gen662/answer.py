try:
    result = int('not a number')
    except (ValueError, TypeError) as e:
        print(f'Caught (ValueError, TypeError): {e}')
    except AttributeError as e:
        print(f'Caught AttributeError: {e}')
    except KeyError as e:
        print(f'Caught KeyError: {e}')
finally:
    print('Cleanup complete')