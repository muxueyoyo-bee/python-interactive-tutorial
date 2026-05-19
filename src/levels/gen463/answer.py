try:
    result = int('not a number')
    except (TypeError, KeyError) as e:
        print(f'Caught (TypeError, KeyError): {e}')
    except AttributeError as e:
        print(f'Caught AttributeError: {e}')
    except KeyError as e:
        print(f'Caught KeyError: {e}')
finally:
    print('Cleanup complete')