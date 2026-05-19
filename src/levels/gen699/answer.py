try:
    result = int('not a number')
    except (OSError, ValueError, KeyError) as e:
        print(f'Caught (OSError, ValueError, KeyError): {e}')
    except ExternallyManagedEnvironment as e:
        print(f'Caught ExternallyManagedEnvironment: {e}')
    except OSError as e:
        print(f'Caught OSError: {e}')
finally:
    print('Cleanup complete')