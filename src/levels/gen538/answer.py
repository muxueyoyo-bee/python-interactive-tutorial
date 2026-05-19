try:
    result = int('not a number')
    except InvalidRequirement as e:
        print(f'Caught InvalidRequirement: {e}')
finally:
    print('Cleanup complete')