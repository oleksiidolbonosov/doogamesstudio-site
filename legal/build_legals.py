import json
from pathlib import Path

LEGAL_DIR = Path(__file__).resolve().parent
TEMPLATES_DIR = LEGAL_DIR / "templates"
OUTPUT_DIR = LEGAL_DIR / "apps"
DATA_FILE = LEGAL_DIR / "apps.json"
ROOT_TERMS = LEGAL_DIR / "terms.html"
ROOT_PRIVACY = LEGAL_DIR / "privacy-policy.html"


def render_template(template_path: Path, context: dict) -> str:
    content = template_path.read_text(encoding="utf-8")
    for placeholder, value in context.items():
        content = content.replace(f"{{{{{placeholder}}}}}", value)
    return content


def main() -> None:
    data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    default_slug = data.get("default_app")
    apps = data.get("apps", [])
    if not apps:
        raise ValueError("No apps defined in apps.json.")
    if default_slug and default_slug not in [app["slug"] for app in apps]:
        raise ValueError("default_app slug not found in apps list.")

    terms_template = TEMPLATES_DIR / "terms-template.html"
    privacy_template = TEMPLATES_DIR / "privacy-template.html"

    for app in apps:
        slug = app["slug"]
        context = {
            "APP_NAME": app["name"],
            "EFFECTIVE_DATE": app["effective_date"],
            "DEVELOPER": app["developer"],
            "CONTACT_EMAIL": app["contact_email"],
        }

        app_dir = OUTPUT_DIR / slug
        app_dir.mkdir(parents=True, exist_ok=True)

        terms_content = render_template(terms_template, context)
        privacy_content = render_template(privacy_template, context)

        (app_dir / "terms.html").write_text(terms_content, encoding="utf-8")
        (app_dir / "privacy-policy.html").write_text(privacy_content, encoding="utf-8")

        if slug == default_slug:
            ROOT_TERMS.write_text(terms_content, encoding="utf-8")
            ROOT_PRIVACY.write_text(privacy_content, encoding="utf-8")


if __name__ == "__main__":
    main()
