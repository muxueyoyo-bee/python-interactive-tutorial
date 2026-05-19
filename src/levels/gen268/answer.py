try:
    result = int('not a number')
    except (TypeError, ValueError) as e:
        print(f'Caught (TypeError, ValueError): {e}')
    except EmptyPage as e:
        print(f'Caught EmptyPage: {e}')
    except PageNotAnInteger as e:
        print(f'Caught PageNotAnInteger: {e}')
finally:
    print('Cleanup complete')