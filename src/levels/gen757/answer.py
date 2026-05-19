try:
    result = int('not a number')
    except InvalidRequirementError as e:
        print(f'Caught InvalidRequirementError: {e}')
    except InvalidVersionError as e:
        print(f'Caught InvalidVersionError: {e}')
    except RuntimeError as e:
        print(f'Caught RuntimeError: {e}')
finally:
    print('Cleanup complete')