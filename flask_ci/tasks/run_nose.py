import os
from flask.ext.script import Option


class Reporter(object):
    @staticmethod
    def get_arguments():
        return [
            Option('--with-xunit', action='store_true', dest='with-xunit', default=False),
            Option('--xunit-file', dest='xunit-file', default=''),
            Option('--with-coverage', action='store_true', dest='with-coverage', default=False),
            Option('--cover-xml', action='store_true', dest='cover-xml', default=False),
            Option('--cover-xml-file', dest='cover-xml-file', default='reports/coverage.xml'),
            Option('--cover-html', action='store_true', dest='cover-xml', default=False),
            Option('--cover-html-dir', dest='cover-html-dir', default='reports/html-coverage'),
            Option('--cover-branches', action='store_true', dest='cover-branches', default=False)
        ]

    def run(self, settings, **options):
        args = list()

        if options['with-xunit']:
            args.append('--with-xunit')
            args.append('--xunit-file=%s' % options['xunit-file'])
        if options['with-coverage']:
            args.append('--with-coverage')
            args.append('--cover-package=%s' % ','.join(getattr(settings, 'PROJECT_APPS', [])))
        if options['cover-xml']:
            args.append('--cover-xml')
            args.append('--cover-xml-file=%s' % options['cover-xml-file'])
        if options['cover-html']:
            args.append('--cover-html')
            args.append('--cover-html-dir=%s' % options['cover-html-dir'])
        if options['cover-branches']:
            args.append('--cover-branches')

        os.system('nosetests %s' % ' '.join(args))

        if options['with-coverage']:
            os.remove('.coverage')
