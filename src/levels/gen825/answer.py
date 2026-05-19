try:
    result = int('not a number')
    except GithubException as e:
        print(f'Caught GithubException: {e}')
finally:
    print('Cleanup complete')