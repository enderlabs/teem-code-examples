# Teem Relay for Google Service Accounts
Teem helps manage conference room space by interacting with existing calendar
systems (Google and Exchange), and syncing that with intelligent tools. You can
learn more about Teem at https://teem.com.

Google Service accounts are different from regular user accounts in several
ways. Two key differences is that they are tied to a custom Google Application
within your own Google Developers portal. The second, is that they can not log
into services, but their credentials can be used to work with Google API's that
are allowed for the application they are associated to. Details on service
accounts and using them as part of Google's OAUTH2.0 authentication flow can be
found at https://developers.google.com/identity/protocols/OAuth2ServiceAccount.

There is a challenge in how Teem interacts with certain calendars when using a
service account. Teem subscribes to [Google Event Watch's](https://developers.google.com/google-apps/calendar/v3/reference/events/watch),
which allows Teem to know when calendars change. This requires subscribing to a
URL that is registered within the application the account is associated to. For
a regular user account that it Teems own application registered in Google, but
for a service account that will be your application that you have created
yourself. Teem will need to then register your url to receive call backs, and
then you need to send those requests on to Teem.

The code examples here are provided to be examples in how to accomplish that,
which you can deploy yourself. You do not have to use these specific examples
to accomplish the requirement outlined above, but this could be a great
starting point to help you.

When cloning this project, please make sure you clone the submodules used in
some examples. To do so add `--recurse-submodules` to your git clone command
such as `git clone --recurse-submodules https://github.com/enderlabs/teem-code-examples`
