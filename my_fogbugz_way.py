import settings

from optparse import OptionParser

parser = OptionParser()
parser.add_option('-s', '--search', dest='search',
        help="Search for the given keywords", metavar="KEYWORDS")

(options, args) = parser.parse_args()

print options
print args

from fogbugz import FogBugz

fb = FogBugz(settings.url)
fb.logon(settings.user_email, settings.user_pass)

if options.search:
    resp = fb.search(q=settings.default_search_prefix + options.search,
                     cols="sTitle,ixPriority,hrsOrigEst,hrsCurrEst,hrsElapsed,ixBugParent"
           )

    for case in resp.cases.childGenerator():
        print case['ixbug'], case.stitle.string
        print case
