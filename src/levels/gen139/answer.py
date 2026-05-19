try:
    result = int('not a number')
    except NoReverseMatch as e:
        print(f'Caught NoReverseMatch: {e}')
    except queryset.model.DoesNotExist as e:
        print(f'Caught queryset.model.DoesNotExist: {e}')
finally:
    print('Cleanup complete')