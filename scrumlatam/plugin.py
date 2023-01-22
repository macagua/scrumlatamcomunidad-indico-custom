import os

from flask_pluginengine import render_plugin_template

from indico.core import signals
from indico.core.plugins import IndicoPlugin, IndicoPluginBlueprint


class ScrumLATAMPlugin(IndicoPlugin):
    """Indico Plugin for Scrum LATAM Comunidad customizations.

    Args:
        IndicoPlugin (IndicoPlugin): Base class for an Indico plugin.

    Returns:
        IndicoPlugin: Base class for an Indico plugin.
    """

    friendly_name = 'Scrum LATAM Comunidad'

    def init(self):
        super(ScrumLATAMPlugin, self).init()

        # Override Indico pages with custom Scrum LATAM Comunidad html
        self.connect(
            signals.plugin.get_template_customization_paths, self._override_templates
        )

        # Inject Scrum LATAM Comunidad specific html into <head> (Open Sans, Fontawesome & Favicon)
        self.template_hook("html-head", self._scrumlatam_head)

        # Inject main css styles
        self.inject_bundle('00-main.css')
        # Inject fonts css styles
        self.inject_bundle('01-fonts.css')
        # Inject footer css styles
        self.inject_bundle('02-footer.css')

        # Inject main javascript
        self.inject_bundle('00-main.js')

    def _override_templates(self, sender, **kwargs):
        """Overrides the Indico templates

        Args:
            sender (_type_): _description_

        Returns:
            string: a string which represents the root path of Indico templates Overrides
        """
        return os.path.join(self.root_path, "indico_template_overrides")

    def _scrumlatam_head(self, **kwargs):
        """Add some specific html into <head> (Open Sans, Fontawesome & Favicon)

        Returns:
            function: Renders a template from the plugin's template folder with the given context.
        """
        return render_plugin_template("head.html")

    def get_blueprints(self):
        return IndicoPluginBlueprint(self.name, __name__)
