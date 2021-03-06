from __future__ import print_function
from .basecommand import BaseCommand


class LDAPUsers(BaseCommand):   # pylint: disable=too-few-public-methods
    """
    Display users in remote directory

    Usage:
        ldapusers [--users=UIDs | --groups=GCNs]

        -u UIDS --users=UIDs    Comma separated list of user uids to provision/sync
        -g GCNs --groups=GCNs   Comma separated list of group common names to provision/sync  # quote names with spaces

    """

    def execute(self):
        self.bind_ldap()

        result = []

        if self.args.get('--users') is None and self.args.get('--groups') is None:
            result = self.ldap_server.get_all_users()
        if self.args.get('--users') is not None:
            users = self.args.get('--users').split(',')
            result = self.ldap_server.get_users_by_uid(users)
        if self.args.get('--groups') is not None:
            groups = self.args.get('--groups').split(',')
            result = self.ldap_server.get_users_by_group(groups)

        print("Retrieving " + str(len(result)) + " user(s) from the directory...")

        self.unbind_ldap()
        for ldap_user in result:
            print(ldap_user.as_dict())
        return True
