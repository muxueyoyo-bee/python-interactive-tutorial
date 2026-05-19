try:
    result = int('not a number')
    except (OSError, ValueError) as e:
        print(f'Caught (OSError, ValueError): {e}')
    except (lxml.etree.XMLSyntaxError, Exception) as e:
        print(f'Caught (lxml.etree.XMLSyntaxError, Exception): {e}')
    except Exception as e:
        print(f'Caught Exception: {e}')
finally:
    print('Cleanup complete')