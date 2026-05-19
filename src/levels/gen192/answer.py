try:
    result = int('not a number')
    except (zipfile.BadZipFile, ET.ParseError) as e:
        print(f'Caught (zipfile.BadZipFile, ET.ParseError): {e}')
    except ET.ParseError as e:
        print(f'Caught ET.ParseError: {e}')
    except Exception as e:
        print(f'Caught Exception: {e}')
finally:
    print('Cleanup complete')