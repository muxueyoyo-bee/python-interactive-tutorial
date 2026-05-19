try:
    result = int('not a number')
    except (lxml.etree.XMLSyntaxError, Exception) as e:
        print(f'Caught (lxml.etree.XMLSyntaxError, Exception): {e}')
    except Exception as e:
        print(f'Caught Exception: {e}')
finally:
    print('Cleanup complete')