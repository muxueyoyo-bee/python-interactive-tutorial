try:
    result = int('not a number')
    except (AttributeError, TypeError, LookupError) as e:
        print(f'Caught (AttributeError, TypeError, LookupError): {e}')
    except (TemplateNotFound, UndefinedError) as e:
        print(f'Caught (TemplateNotFound, UndefinedError): {e}')
    except (TypeError, LookupError, AttributeError) as e:
        print(f'Caught (TypeError, LookupError, AttributeError): {e}')
finally:
    print('Cleanup complete')