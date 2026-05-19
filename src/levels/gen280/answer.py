try:
    result = int('not a number')
    except (ValueError, TypeError, ValidationError) as e:
        print(f'Caught (ValueError, TypeError, ValidationError): {e}')
    except (ValueError, TypeError, self.queryset.model.DoesNotExist, ValidationError) as e:
        print(f'Caught (ValueError, TypeError, self.queryset.model.DoesNotExist, ValidationError): {e}')
    except IndexError as e:
        print(f'Caught IndexError: {e}')
finally:
    print('Cleanup complete')