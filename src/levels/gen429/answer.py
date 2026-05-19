try:
    result = int('not a number')
    except BadSignature as e:
        print(f'Caught BadSignature: {e}')
finally:
    print('Cleanup complete')