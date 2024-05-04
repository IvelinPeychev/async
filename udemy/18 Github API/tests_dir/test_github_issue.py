from creds import *
from playwright.sync_api import APIRequestContext, Page


def test_create_issue(api_context: APIRequestContext):
    issue_data = {
        'title': '[BUG] That Went Wrong',
        'body': 'When doing this, that failed',
        # 'assignee': 'Ivelin Peychev',
        # 'label': 'Bug'
    }

    post_response = api_context.post(
        f'/repos/{GITHUB_USER}/{GITHUB_REPO}/issues', data=issue_data
    )
    assert post_response.ok


def test_take_issue_screenshot(page: Page):
    page.goto(f'https://github.com/{GITHUB_USER}/{GITHUB_REPO}/issues')
    page.screenshot(path='issues.jpeg', full_page=True)


def test_issue_in_repo(api_context: APIRequestContext):
    issues = api_context.get(f'/repos/{GITHUB_USER}/{GITHUB_REPO}/issues')
    assert issues.ok

    new_issue = [issue for issue in issues.json() if issue['title'] == '[BUG] That Went Wrong'][0]

    assert new_issue['body'] == 'When doing this, that failed'
