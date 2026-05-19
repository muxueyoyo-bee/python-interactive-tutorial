try:
    result = int('not a number')
    except InvalidMarkerError as e:
        print(f'Caught InvalidMarkerError: {e}')
    except InvalidRequirementError as e:
        print(f'Caught InvalidRequirementError: {e}')
    except IsolatedBuildBackendError as e:
        print(f'Caught IsolatedBuildBackendError: {e}')
finally:
    print('Cleanup complete')