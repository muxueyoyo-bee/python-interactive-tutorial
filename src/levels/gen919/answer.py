try:
    result = int('not a number')
    except (exc.PendingRollbackError, exc.ResourceClosedError) as e:
        print(f'Caught (exc.PendingRollbackError, exc.ResourceClosedError): {e}')
    except AttributeError as e:
        print(f'Caught AttributeError: {e}')
    except BaseException as e:
        print(f'Caught BaseException: {e}')
finally:
    print('Cleanup complete')