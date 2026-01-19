---
name: updating-plugin-versions
description: A skill for updating Claude Code Plugin versions. Automatically increments the patch version when the user says "update patch version", the major version when the user says "update major version", and the minor version when the user says "update minor version". This skill automatically finds all files that need version updates and synchronizes them.
---

# Plugin Version Update Skill

This skill manages Claude Code Plugin version updates, following Semantic Versioning (SemVer) specification.

## Version Number Format

The version number format is `MAJOR.MINOR.PATCH`, e.g., `2.27.0`:

- **MAJOR**: Incompatible API changes or major feature refactoring
- **MINOR**: Backward-compatible new feature additions
- **PATCH**: Backward-compatible bug fixes

## Trigger Conditions

This skill is automatically triggered when the user mentions the following keywords:

| User Command | Version Update Type | Example Change |
|--------------|---------------------|----------------|
| "update patch version" / "patch" / "fix version" | PATCH +1 | 2.27.0 → 2.27.1 |
| "update minor version" / "minor" / "feature version" | MINOR +1, PATCH reset to 0 | 2.27.0 → 2.28.0 |
| "update major version" / "major" / "breaking version" | MAJOR +1, MINOR/PATCH reset to 0 | 2.27.0 → 3.0.0 |

## Files to Update

According to the Claude Code Plugin official specification, version information is stored in the following locations:

### 1. Plugin Configuration File (plugin.json)

**Path**: `plugins/native-engineering/.claude-plugin/plugin.json`

```json
{
  "name": "native-engineering",
  "version": "2.27.0",  // ← Update here
  "description": "..."
}
```

### 2. Marketplace Configuration File (marketplace.json)

**Path**: `.claude-plugin/marketplace.json`

```json
{
  "plugins": [
    {
      "name": "native-engineering",
      "version": "2.27.0",  // ← Update here
      ...
    }
  ]
}
```

### 3. Changelog (CHANGELOG.md)

**Path**: `plugins/native-engineering/CHANGELOG.md`

Add a new version entry at the top of the file:

```markdown
## [X.Y.Z] - YYYY-MM-DD

### Added
- New feature description

### Changed
- Change description

### Fixed
- Fix description
```

## Execution Flow

### Step 1: Read Current Version

Read the current version number from `plugins/native-engineering/.claude-plugin/plugin.json`.

### Step 2: Calculate New Version

Calculate the new version number based on the user's command type:

```
Current version: MAJOR.MINOR.PATCH

Update patch version:  → MAJOR.MINOR.(PATCH+1)
Update minor version:  → MAJOR.(MINOR+1).0
Update major version:  → (MAJOR+1).0.0
```

### Step 3: Update All Version Files

**The following files must be updated synchronously:**

1. ✅ `plugins/native-engineering/.claude-plugin/plugin.json` - `version` field
2. ✅ `.claude-plugin/marketplace.json` - corresponding plugin's `version` field

### Step 4: Update CHANGELOG.md

Insert a new version entry at the top of the `plugins/native-engineering/CHANGELOG.md` file.

Use the current date (YYYY-MM-DD format) and add appropriate change descriptions based on version type:

- **PATCH**: Default to `### Fixed` category
- **MINOR**: Default to `### Added` category  
- **MAJOR**: Default to `### Changed` and `### Breaking Changes` categories

### Step 5: Verify

Ensure version numbers are consistent across all files:

```bash
# Verify JSON file format
cat plugins/native-engineering/.claude-plugin/plugin.json | jq .version
cat .claude-plugin/marketplace.json | jq '.plugins[] | select(.name=="native-engineering") | .version'
```

## Example Operations

### User Input: "update patch version"

**Execution Steps:**

1. Read current version: `2.27.0`
2. Calculate new version: `2.27.1`
3. Update `plugin.json`: `"version": "2.27.1"`
4. Update `marketplace.json`: corresponding plugin `"version": "2.27.1"`
5. Update `CHANGELOG.md`: Add `## [2.27.1] - 2024-XX-XX` entry
6. Output confirmation message

### User Input: "update major version"

**Execution Steps:**

1. Read current version: `2.27.0`
2. Calculate new version: `3.0.0`
3. Update all version files
4. Add Breaking Changes note in CHANGELOG
5. Output confirmation message

## Notes

1. **Version Consistency**: Version numbers must be exactly the same across all files
2. **JSON Format Validation**: Use `jq` to verify JSON file format after updates
3. **CHANGELOG Format**: Follow [Keep a Changelog](https://keepachangelog.com/) specification
4. **Semantic Versioning**: Strictly follow [SemVer](https://semver.org/) specification

## Related Resources

- [Claude Code Plugin Documentation](https://docs.claude.com/en/docs/claude-code/plugins)
- [Plugin Reference](https://docs.claude.com/en/docs/claude-code/plugins-reference)
- [Semantic Versioning](https://semver.org/)
- [Keep a Changelog](https://keepachangelog.com/)
