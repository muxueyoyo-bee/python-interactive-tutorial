try:
    result = int('not a number')
    except (TypeError, StopIteration) as e:
        print(f'Caught (TypeError, StopIteration): {e}')
    except (ValueError, OverflowError) as e:
        print(f'Caught (ValueError, OverflowError): {e}')
    except AttributeError as e:
        print(f'Caught AttributeError: {e}')
finally:
    print('Cleanup complete')