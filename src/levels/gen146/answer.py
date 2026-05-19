try:
    result = int('not a number')
    except (KeyError, UnicodeDecodeError, TypeError, UnpicklingError) as e:
        print(f'Caught (KeyError, UnicodeDecodeError, TypeError, UnpicklingError): {e}')
    except (KeyError, UnicodeDecodeError, TypeError, UnpicklingError) + dbm.error as e:
        print(f'Caught (KeyError, UnicodeDecodeError, TypeError, UnpicklingError) + dbm.error: {e}')
    except (KeyboardInterrupt, SystemExit) as e:
        print(f'Caught (KeyboardInterrupt, SystemExit): {e}')
finally:
    print('Cleanup complete')