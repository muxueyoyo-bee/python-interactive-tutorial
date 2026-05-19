try:
    result = int('not a number')
    except MailerDoesNotExist as e:
        print(f'Caught MailerDoesNotExist: {e}')
finally:
    print('Cleanup complete')