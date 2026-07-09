def test_user_profile_first_login(login):

    profile = UserProfilePage(login.driver)

    profile.verify_user_profile_screen()


def test_mobile_number_prefill(login):

    profile = UserProfilePage(login.driver)

    profile.verify_mobile_number_prefill()


def test_email_prefill(login):

    profile = UserProfilePage(login.driver)

    profile.verify_email_prefill()


def test_complete_mandatory_profile_details(login):

    profile = UserProfilePage(login.driver)

    profile.complete_mandatory_profile_details()