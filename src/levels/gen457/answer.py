try:
    result = int('not a number')
    except (ValueError, KeyError) as e:
        print(f'Caught (ValueError, KeyError): {e}')
    except AttributeError as e:
        print(f'Caught AttributeError: {e}')
    except ImportError as e:
        print(f'Caught ImportError: {e}')
finally:
    print('Cleanup complete')