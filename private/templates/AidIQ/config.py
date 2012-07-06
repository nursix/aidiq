# -*- coding: utf-8 -*-

from gluon import current, URL
from gluon.storage import Storage
from gluon.contrib.simplejson.ordered_dict import OrderedDict
settings = current.deployment_settings
T = current.T

"""
    Template settings for AidIQ
"""

# Pre-Populate
settings.base.prepopulate = ["AidIQ"]

# Theme
settings.base.theme = "AidIQ"

# Security Policy
settings.security.policy = 7 # Organisation-ACLs

settings.auth.login_next = URL(c="project", f="task", vars={"mine":1})

# L10n settings
settings.L10n.languages = OrderedDict([
    ("en-gb", "English"),
])
# Default Language
settings.L10n.default_language = "en-gb"
# Uncomment to Hide the language toolbar
settings.L10n.display_toolbar = False
# Number formats (defaults to ISO 31-0)
# Decimal separator for numbers (defaults to ,)
settings.L10n.decimal_separator = "."
# Thousands separator for numbers (defaults to space)
settings.L10n.thousands_separator = ","

# Uncomment this to request the Organisation when a user registers
settings.auth.registration_requests_organisation = True
# Uncomment this to have the Organisation selection during registration be mandatory
settings.auth.registration_organisation_mandatory = True

# Projects
# Uncomment this to use settings suitable for detailed Task management
settings.project.mode_task = True
# Uncomment this to use Activities for projects
settings.project.activities = True
# Uncomment this to use Milestones in project/task.
settings.project.milestones = True
# Uncomment this to disable Sectors in projects
settings.project.sectors = False

# Frontpage settings
# RSS feeds
#deployment_settings.frontpage.rss = [
#    {"title": "Blog",
#     # Drupal Blog
#     "url": "http://aidiq.com/blog/feed"
#    },
#    {"title": "Twitter",
#     # Use idfromuser.com to determine the ID
#     # @SahanaFOSS
#     "url": "http://twitter.com/statuses/user_timeline/80964032.rss"
#     # Hashtag
#     #url: "http://search.twitter.com/search.atom?q=%23eqnz"
#    }
#]

# Comment/uncomment modules here to disable/enable them
settings.modules = OrderedDict([
    # Core modules which shouldn't be disabled
    ("default", Storage(
            name_nice = T("Home"),
            restricted = False, # Use ACLs to control access to this module
            access = None,      # All Users (inc Anonymous) can see this module in the default menu & access the controller
            module_type = None  # This item is not shown in the menu
        )),
    ("admin", Storage(
            name_nice = T("Administration"),
            #description = "Site Administration",
            restricted = True,
            access = "|1|",     # Only Administrators can see this module in the default menu & access the controller
            module_type = None  # This item is handled separately for the menu
        )),
    ("appadmin", Storage(
            name_nice = T("Administration"),
            #description = "Site Administration",
            restricted = True,
            module_type = None  # No Menu
        )),
    ("errors", Storage(
            name_nice = T("Ticket Viewer"),
            #description = "Needed for Breadcrumbs",
            restricted = False,
            module_type = None  # No Menu
        )),
    ("sync", Storage(
            name_nice = T("Synchronization"),
            #description = "Synchronization",
            restricted = True,
            access = "|1|",     # Only Administrators can see this module in the default menu & access the controller
            module_type = None  # This item is handled separately for the menu
        )),
    ("gis", Storage(
            name_nice = T("Map"),
            #description = "Situation Awareness & Geospatial Analysis",
            restricted = True,
            module_type = None,     # 6th item in the menu
        )),
    ("pr", Storage(
            name_nice = T("Person Registry"),
            #description = "Central point to record details on People",
            restricted = True,
            access = "|1|",     # Only Administrators can see this module in the default menu (access to controller is possible to all still)
            module_type = None
        )),
    ("org", Storage(
            name_nice = T("Organizations"),
            #description = 'Lists "who is doing what & where". Allows relief agencies to coordinate their activities',
            restricted = True,
            module_type = None
        )),
    # All modules below here should be possible to disable safely
    ("hrm", Storage(
            name_nice = T("Staff"),
            #description = "Human Resources Management",
            restricted = True,
            module_type = None,
        )),
    ("cms", Storage(
          name_nice = T("Content Management"),
          #description = "Content Management System",
          restricted = True,
          module_type = None,
      )),
    ("doc", Storage(
            name_nice = T("Documents"),
            #description = "A library of digital resources, such as photos, documents and reports",
            restricted = True,
            module_type = None,
        )),
    ("msg", Storage(
            name_nice = T("Messaging"),
            #description = "Sends & Receives Alerts via Email & SMS",
            restricted = True,
            # The user-visible functionality of this module isn't normally required. Rather it's main purpose is to be accessed from other modules.
            module_type = None,
        )),
    ("project", Storage(
            name_nice = T("Projects"),
            #description = "Tracking of Projects, Activities and Tasks",
            restricted = True,
            module_type = 1
        )),
    #("survey", Storage(
    #        name_nice = T("Surveys"),
    #        #description = "Create, enter, and manage surveys.",
    #        restricted = True,
    #        module_type = 5,
    #    )),
])