try:
    result = int('not a number')
    except (lxml.etree.XMLSyntaxError, Exception) as e:
        print(f'Caught (lxml.etree.XMLSyntaxError, Exception): {e}')
    except Exception as e:
        print(f'Caught Exception: {e}')
    except ValueError as e:
        print(f'Caught ValueError: {e}')
finally:
    print('Cleanup complete')