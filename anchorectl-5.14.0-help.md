# AnchoreCTL Command Line Reference

Generated on: 2025-02-13 15:21:01

## Version Information

```
Application:        anchorectl
Version:            5.14.0
SyftVersion:        v1.19.0
BuildDate:          2025-01-29T18:49:44Z
GitCommit:          2ec6095c00c18dfe1a105b90da29864a7d9ac93d
GitDescription:     v5.14.0
Platform:           linux/amd64
GoVersion:          go1.23.5
Compiler:           gc
```


## anchorectl account

```text
Account related operations

Usage:
  anchorectl account [command]

Available Commands:
  add         Create a new account
  delete      Delete the specified account, only allowed if the account is in the disabled state
  disable     Disable an account
  enable      Enable a previously disabled account
  get         Get info about an account
  list        List account summaries
  update      Update an account

Flags:
  -h, --help   help for account

Use "anchorectl account [command] --help" for more information about a command.

For help regarding global flags, run --help on the root command
```


### anchorectl account add

```text
Create a new account. Only available to admin user.

Usage:
  anchorectl account add NAME [flags]

Flags:
      --email string    the account email (env: ANCHORECTL_ACCOUNT_EMAIL)
  -h, --help            help for add
  -o, --output string   the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")

For help regarding global flags, run --help on the root command
```


### anchorectl account delete

```text
Delete the specified account, only allowed if the account is in the disabled state. All users will be deleted along with the account and all resources will be garbage collected

Usage:
  anchorectl account delete NAME [flags]

Arguments:
  NAME:  name of the account

Aliases:
  delete, del

Flags:
  -h, --help            help for delete
  -o, --output string   the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")

For help regarding global flags, run --help on the root command
```


### anchorectl account disable

```text
Disable an account

Usage:
  anchorectl account disable NAME [flags]

Arguments:
  NAME:  name of the account

Flags:
  -h, --help            help for disable
  -o, --output string   the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")

For help regarding global flags, run --help on the root command
```


### anchorectl account enable

```text
Enable a previously disabled account

Usage:
  anchorectl account enable NAME [flags]

Arguments:
  NAME:  name of the account

Flags:
  -h, --help            help for enable
  -o, --output string   the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")

For help regarding global flags, run --help on the root command
```


### anchorectl account get

```text
Get info about an account. Only available to admin user. Uses the main user Id, not a username.

Usage:
  anchorectl account get NAME [flags]

Arguments:
  NAME:  name of account

Flags:
  -h, --help            help for get
  -o, --output string   the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")

For help regarding global flags, run --help on the root command
```


### anchorectl account list

```text
List account summaries. Only available to the system admin user.

Usage:
  anchorectl account list [flags]

Flags:
  -h, --help            help for list
  -o, --output string   the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")
      --state string    filter accounts by state (allowable: [enabled disabled deleting]; env: ANCHORECTL_ACCOUNT_STATE)

For help regarding global flags, run --help on the root command
```


### anchorectl account update

```text
Update an account. Only available to admin user.

Usage:
  anchorectl account update NAME [flags]

Arguments:
  NAME:  name of the account

Flags:
      --email string    the account email (env: ANCHORECTL_ACCOUNT_EMAIL)
  -h, --help            help for update
  -o, --output string   the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")

For help regarding global flags, run --help on the root command
```


## anchorectl airgap

```text
Airgap related operations

Usage:
  anchorectl airgap [command]

Available Commands:
  feed        Feed related operations

Flags:
  -h, --help   help for airgap

Use "anchorectl airgap [command] --help" for more information about a command.

For help regarding global flags, run --help on the root command
```


### anchorectl airgap feed

```text
Feed related operations

Usage:
  anchorectl airgap feed [command]

Available Commands:
  download    Check for updates to Hosted Feeds and download the latest changes
  upload      Upload the specified feedset into Anchore Enterprise

Flags:
  -h, --help   help for feed

Use "anchorectl airgap feed [command] --help" for more information about a command.

For help regarding global flags, run --help on the root command
```


#### anchorectl airgap feed download

```text
Check for updates to Hosted Feeds and download the latest changes

Usage:
  anchorectl airgap feed download [flags]

Flags:
  -f, --file string      the file path to create or update a feedset archive (env: ANCHORECTL_FEEDS_FILE)
  -h, --help             help for download
  -k, --key string       the api key to authorize the request (env: ANCHORECTL_API_KEY)
  -l, --license string   the path to an Anchore license file (env: ANCHORECTL_LICENSE_FILE)
  -o, --output string    the format to show the results (allowable: [text json json-raw]; env: ANCHORECTL_FORMAT) (default "text")

For help regarding global flags, run --help on the root command
```


#### anchorectl airgap feed upload

```text
Upload the specified feedset into Anchore Enterprise

Usage:
  anchorectl airgap feed upload [flags]

Flags:
  -f, --file string     path to a previously downloaded feedset archive (env: ANCHORECTL_INPUT_FILE)
      --force           perform feed upload even if checksums match (env: ANCHORECTL_FORCE)
  -h, --help            help for upload
  -o, --output string   the format to show the results (allowable: [text json json-raw]; env: ANCHORECTL_FORMAT) (default "text")

For help regarding global flags, run --help on the root command
```


## anchorectl application

```text
Application related operations

Usage:
  anchorectl application [command]

Available Commands:
  add         Create an application
  artifact    Application version artifact management operations
  delete      Delete an application by application_id
  get         Get an application by application_id
  list        List all applications
  sbom        Get the combined sbom for the given application version, optionally filtered by artifact type
  update      Updates application details for given application_id
  version     Application version related operations

Flags:
  -h, --help   help for application

Use "anchorectl application [command] --help" for more information about a command.

For help regarding global flags, run --help on the root command
```


### anchorectl application add

```text
Create an application

Usage:
  anchorectl application add NAME [flags]

Arguments:
  NAME:  the name of the application

Flags:
      --description string   the description of the application (env: ANCHORECTL_APPLICATION_DESCRIPTION)
  -h, --help                 help for add
  -i, --input string         path to a JSON input file or - to read from stdin (env: ANCHORECTL_INPUT)
  -o, --output string        the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")

For help regarding global flags, run --help on the root command
```


### anchorectl application artifact

```text
Application version artifact management operations

Usage:
  anchorectl application artifact [command]

Available Commands:
  add         Add artifact to an application version
  list        List artifacts present on a given application version
  remove      Delete an artifact from an application version

Flags:
  -h, --help   help for artifact

Use "anchorectl application artifact [command] --help" for more information about a command.

For help regarding global flags, run --help on the root command
```


#### anchorectl application artifact add

```text
Add artifact to an application version

Usage:
  anchorectl application artifact add APPLICATION_VERSION TYPE ARTIFACT [flags]

Arguments:
  APPLICATION_VERSION:  the application version in the format <application-name>@<version-name>
  ARTIFACT:  the ID of an artifact or for image: full image tag or sha256, for source: revision
  TYPE:  the artifact type (allowable values: [image source])

Flags:
  -h, --help            help for add
  -o, --output string   the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")

For help regarding global flags, run --help on the root command
```


#### anchorectl application artifact list

```text
List artifacts present on a given application version

Usage:
  anchorectl application artifact list APPLICATION_VERSION [flags]

Arguments:
  APPLICATION_VERSION:  the application version in the format <application-name>@<version-name>

Flags:
  -h, --help               help for list
  -o, --output string      the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")
      --type stringArray   filter results to specific artifact types (allowable: [image source]) (default [image,source])

For help regarding global flags, run --help on the root command
```


#### anchorectl application artifact remove

```text
Delete an artifact from an application version

Usage:
  anchorectl application artifact remove APPLICATION_VERSION ARTIFACT [flags]

Arguments:
  APPLICATION_VERSION:  the application version in the format <application-name>@<version-name>
  ARTIFACT:  the ID of an artifact or sha256 for an image, revision if source

Flags:
  -h, --help            help for remove
  -o, --output string   the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")

For help regarding global flags, run --help on the root command
```


### anchorectl application delete

```text
Delete an application by application_id

Usage:
  anchorectl application delete APPLICATION [flags]

Arguments:
  APPLICATION:  the application name or ID

Aliases:
  delete, del

Flags:
  -h, --help            help for delete
  -o, --output string   the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")

For help regarding global flags, run --help on the root command
```


### anchorectl application get

```text
Get an application by application_id

Usage:
  anchorectl application get APPLICATION [flags]

Arguments:
  APPLICATION:  the application name or ID

Flags:
  -h, --help               help for get
      --include-versions   include version information (env: ANCHORECTL_APPLICATION_INCLUDE_VERSIONS) (default true)
  -o, --output string      the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")

For help regarding global flags, run --help on the root command
```


### anchorectl application list

```text
List all applications

Usage:
  anchorectl application list [flags]

Flags:
  -h, --help               help for list
      --include-versions   include version information (env: ANCHORECTL_APPLICATION_INCLUDE_VERSIONS) (default true)
  -o, --output string      the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")

For help regarding global flags, run --help on the root command
```


### anchorectl application sbom

```text
Get the combined sbom for the given application version, optionally filtered by artifact type

Usage:
  anchorectl application sbom APPLICATION_VERSION [flags]

Arguments:
  APPLICATION_VERSION:  the application and version to add

Flags:
  -h, --help               help for sbom
      --type stringArray   filter results to specific artifact types  (allowable: [image source]) (default [image,source])

For help regarding global flags, run --help on the root command
```


### anchorectl application update

```text
Updates application details for given application_id

Usage:
  anchorectl application update APPLICATION [flags]

Arguments:
  APPLICATION:  the application name or ID

Flags:
      --description string   the description of the application (env: ANCHORECTL_APPLICATION_DESCRIPTION)
  -h, --help                 help for update
  -i, --input string         path to a JSON input file or - to read from stdin (env: ANCHORECTL_INPUT)
      --name string          the name of the application (env: ANCHORECTL_APPLICATION_NAME)
  -o, --output string        the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")

For help regarding global flags, run --help on the root command
```


### anchorectl application version

```text
Manage application versions

Usage:
  anchorectl application version [command]

Available Commands:
  add             Create an application version
  delete          Delete an application version
  get             Get an application version
  list            List all application verions
  update          Updates application version details
  vulnerabilities Get the vulnerabilities for a given application version

Flags:
  -h, --help   help for version

Use "anchorectl application version [command] --help" for more information about a command.

For help regarding global flags, run --help on the root command
```


#### anchorectl application version add

```text
Create an application version

Usage:
  anchorectl application version add APPLICATION_VERSION [flags]

Arguments:
  APPLICATION_VERSION:  the application version to add in the format <application-name>@<version-name>

Flags:
  -h, --help            help for add
  -o, --output string   the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")

For help regarding global flags, run --help on the root command
```


#### anchorectl application version delete

```text
Delete an application version

Usage:
  anchorectl application version delete APPLICATION_VERSION [flags]

Arguments:
  APPLICATION_VERSION:  the application version in the format <application-name>@<version-name>

Aliases:
  delete, del

Flags:
  -h, --help            help for delete
  -o, --output string   the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")

For help regarding global flags, run --help on the root command
```


#### anchorectl application version get

```text
Get an application version

Usage:
  anchorectl application version get APPLICATION_VERSION [flags]

Arguments:
  APPLICATION_VERSION:  the application version in the format <application-name>@<version-name>

Flags:
  -h, --help            help for get
  -o, --output string   the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")

For help regarding global flags, run --help on the root command
```


#### anchorectl application version list

```text
List all application verions

Usage:
  anchorectl application version list APPLICATION [flags]

Arguments:
  APPLICATION:  the application to list versions for

Flags:
  -h, --help            help for list
  -o, --output string   the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")

For help regarding global flags, run --help on the root command
```


#### anchorectl application version update

```text
Updates application version details

Usage:
  anchorectl application version update APPLICATION_VERSION [flags]

Arguments:
  APPLICATION_VERSION:  the application version in the format <application-name>@<version-name>

Flags:
  -h, --help            help for update
      --name string     the name of the application (env: ANCHORECTL_APPLICATION_VERSION_NAME)
  -o, --output string   the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")

For help regarding global flags, run --help on the root command
```


#### anchorectl application version vulnerabilities

```text
Get the vulnerabilities for a given application version

Usage:
  anchorectl application version vulnerabilities APPLICATION_VERSION [flags]

Arguments:
  APPLICATION_VERSION:  the application version in the format <application-name>@<version-name>

Aliases:
  vulnerabilities, vulns, vuln

Flags:
  -h, --help            help for vulnerabilities
  -o, --output string   the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")
      --will-not-fix    (env: ANCHORECTL_WILL_NOT_FIX)

For help regarding global flags, run --help on the root command
```


## anchorectl archive

```text
Archive rule and image operations

Usage:
  anchorectl archive [command]

Available Commands:
  image       Archive image related operations
  rule        Archive rule related operations

Flags:
  -h, --help   help for archive

Use "anchorectl archive [command] --help" for more information about a command.

For help regarding global flags, run --help on the root command
```


### anchorectl archive image

```text
Archive image related operations

Usage:
  anchorectl archive image [command]

Available Commands:
  add         Archives Images
  delete      Performs a synchronous archive deletion
  get         Returns the archive metadata record identifying the image and tags for the analysis in the archive
  list        List archived images
  restore     Creates a new analysis task that is executed asynchronously

Flags:
  -h, --help   help for image

Use "anchorectl archive image [command] --help" for more information about a command.

For help regarding global flags, run --help on the root command
```


#### anchorectl archive image add

```text
Archive images

Usage:
  anchorectl archive image add IMAGE_DIGESTS [flags]

Arguments:
  IMAGE_DIGESTS:  List of image digests to archive

Flags:
  -h, --help            help for add
  -o, --output string   the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")

For help regarding global flags, run --help on the root command
```


#### anchorectl archive image delete

```text
Performs a synchronous archive deletion

Usage:
  anchorectl archive image delete IMAGEDIGEST [flags]

Arguments:
  IMAGEDIGEST:  image digest to delete from archive

Aliases:
  delete, del

Flags:
      --force           force archive image deletion (env: ANCHORECTL_ARCHIVE_IMAGE_FORCE)
  -h, --help            help for delete
  -o, --output string   the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")

For help regarding global flags, run --help on the root command
```


#### anchorectl archive image get

```text
Returns the archive metadata record identifying the image and tags for the analysis in the archive.

Usage:
  anchorectl archive image get IMAGE_DIGEST [flags]

Arguments:
  IMAGE_DIGEST:  The image digest to identify the image analysis

Flags:
  -h, --help            help for get
  -o, --output string   the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")

For help regarding global flags, run --help on the root command
```


#### anchorectl archive image list

```text
List archived images

Usage:
  anchorectl archive image list [flags]

Flags:
  -h, --help            help for list
  -o, --output string   the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")

For help regarding global flags, run --help on the root command
```


#### anchorectl archive image restore

```text
Creates a new analysis task that is executed asynchronously

Usage:
  anchorectl archive image restore DIGEST [flags]

Arguments:
  DIGEST:  The image digest identify the analysis. Archived analyses are based on digest, tag records are restored as analysis is restored.

Flags:
      --force           override any existing entry in the system (env: ANCHORECTL_ARCHIVE_IMAGE_FORCE)
  -h, --help            help for restore
  -o, --output string   the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")

For help regarding global flags, run --help on the root command
```


### anchorectl archive rule

```text
Archive rule related operations

Usage:
  anchorectl archive rule [command]

Available Commands:
  add         Add an analysis archive rule
  delete      Delete an analysis archive rule
  get         Get an analysis archive rule
  list        List the analysis archive rules

Flags:
  -h, --help   help for rule

Use "anchorectl archive rule [command] --help" for more information about a command.

For help regarding global flags, run --help on the root command
```


#### anchorectl archive rule add

```text
Add an analysis archive rule

Usage:
  anchorectl archive rule add [flags]

Flags:
      --analysis-age-days int32              matches if the analysis is strictly older than this number of days
                                             (env: ANCHORECTL_ARCHIVE_RULE_ANALYSIS_AGE_DAYS)
      --exclude-expiration-days int32        how long the image selected will be excluded from the archive transition
                                             (env: ANCHORECTL_ARCHIVE_RULE_EXCLUDE_EXPIRATION_DAYS)
      --exclude-last-seen-in-days int32      exclude image from archive if last seen in inventory within defined number of days
                                             (env: ANCHORECTL_ARCHIVE_RULE_EXCLUDE_LAST_SEEN_IN_DAYS)
      --exclude-selector-registry string     the registry section of a pull string. e.g. with "docker.io/anchore/anchore-engine:latest", this is "docker.io"
                                             (env: ANCHORECTL_ARCHIVE_RULE_EXCLUDE_SELECTOR_REGISTRY)
      --exclude-selector-repository string   the repository section of a pull string. e.g. with "docker.io/anchore/anchore-engine:latest", this is "anchore/anchore-engine"
                                             (env: ANCHORECTL_ARCHIVE_RULE_EXCLUDE_SELECTOR_REPOSITORY)
      --exclude-selector-tag string          the tag-only section of a pull string. e.g. with "docker.io/anchore/anchore-engine:latest", this is "latest"
                                             (env: ANCHORECTL_ARCHIVE_RULE_EXCLUDE_SELECTOR_TAG)
  -h, --help                                 help for add
  -i, --input string                         path to a JSON input file or - to read from stdin (env: ANCHORECTL_INPUT)
      --max-images-per-account int32         this is the maximum number of image analyses an account can have. Can only be set on system_global rules
                                             (env: ANCHORECTL_ARCHIVE_RULE_MAX_IMAGES_PER_ACCOUNT)
  -o, --output string                        the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")
      --rule-id string                       unique identifier for archive rule (env: ANCHORECTL_ARCHIVE_RULE_RULE_ID)
      --selector-registry string             the registry section of a pull string. e.g. with "docker.io/anchore/anchore-engine:latest", this is "docker.io"
                                             (env: ANCHORECTL_ARCHIVE_RULE_SELECTOR_REGISTRY) (default "*")
      --selector-repository string           the repository section of a pull string. e.g. with "docker.io/anchore/anchore-engine:latest", this is "anchore/anchore-engine"
                                             (env: ANCHORECTL_ARCHIVE_RULE_SELECTOR_REPOSITORY) (default "*")
      --selector-tag string                  the tag-only section of a pull string. e.g. with "docker.io/anchore/anchore-engine:latest", this is "latest"
                                             (env: ANCHORECTL_ARCHIVE_RULE_SELECTOR_TAG) (default "*")
      --system-global                        true if the rule applies to all accounts in the system. This is only available to admin users to update/modify, but all users with permission to list rules can see them
                                             (env: ANCHORECTL_ARCHIVE_RULE_SYSTEM_GLOBAL)
      --tag-versions-newer int32             number of images mapped to the tag that are newer (env: ANCHORECTL_ARCHIVE_RULE_TAG_VERSIONS_NEWER)
      --transition string                    the type of transition to make. If "archive", then archive an image from the working set and remove it from the working set. If "delete", then match against archived images and delete from the archive if match.
                                             (allowable: [archive delete]; env: ANCHORECTL_ARCHIVE_RULE_TRANSITION)

For help regarding global flags, run --help on the root command
```


#### anchorectl archive rule delete

```text
Delete an analysis archive rule

Usage:
  anchorectl archive rule delete ID [flags]

Arguments:
  ID:  the rule id

Aliases:
  delete, del

Flags:
  -h, --help            help for delete
  -o, --output string   the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")

For help regarding global flags, run --help on the root command
```


#### anchorectl archive rule get

```text
Get an analysis archive rule

Usage:
  anchorectl archive rule get ID [flags]

Arguments:
  ID:  the rule id

Flags:
  -h, --help            help for get
  -o, --output string   the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")

For help regarding global flags, run --help on the root command
```


#### anchorectl archive rule list

```text
List the analysis archive rules

Usage:
  anchorectl archive rule list [flags]

Flags:
      --global          include system global rules (owned by admin) even for non-admin users
                        (env: ANCHORECTL_ARCHIVE_RULE_GLOBAL) (default true)
  -h, --help            help for list
  -o, --output string   the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")

For help regarding global flags, run --help on the root command
```


## anchorectl correction

```text
Correction related operations

Usage:
  anchorectl correction [command]

Available Commands:
  add         Add a correction record that will be used to fix false positive vulnerabilities
  delete      Delete a single correction, looked up via it's uuid
  get         Returns a single correction, looked up via it's uuid
  list        Returns a list of corrections

Flags:
  -h, --help   help for correction

Use "anchorectl correction [command] --help" for more information about a command.

For help regarding global flags, run --help on the root command
```


### anchorectl correction add

```text
Add a correction record that will be used to fix false positive vulnerabilities

Usage:
  anchorectl correction add [flags]

Flags:
      --description string   optional description of this correction rule (env: ANCHORECTL_CORRECTION_DESCRIPTION)
  -h, --help                 help for add
  -i, --input string         path to a JSON input file or - to read from stdin (env: ANCHORECTL_INPUT)
      --match strings        matches of the form key=vlue (e.g. package=spring-core) (env: ANCHORECTL_CORRECTION_MATCH)
  -o, --output string        the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")
      --replace strings      replacements of the form key=vlue (e.g. cpes=cpe:2.3:a:pivotal_software:spring_framework:3.2.14:*:*:*:*:*:*:*)
                             (env: ANCHORECTL_CORRECTION_REPLACE)
      --type string          type of match [supports os, npm, gem, python, java, go] (env: ANCHORECTL_CORRECTION_TYPE)

For help regarding global flags, run --help on the root command
```


### anchorectl correction delete

```text
Delete a single correction, looked up via it's uuid

Usage:
  anchorectl correction delete ID [flags]

Arguments:
  ID:  the correction ID

Aliases:
  delete, del

Flags:
  -h, --help            help for delete
  -o, --output string   the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")

For help regarding global flags, run --help on the root command
```


### anchorectl correction get

```text
Returns a single correction, looked up via it's uuid

Usage:
  anchorectl correction get ID [flags]

Arguments:
  ID:  the correction ID

Flags:
  -h, --help            help for get
  -o, --output string   the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")

For help regarding global flags, run --help on the root command
```


### anchorectl correction list

```text
Returns a list of corrections

Usage:
  anchorectl correction list [flags]

Flags:
  -h, --help            help for list
  -o, --output string   the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")

For help regarding global flags, run --help on the root command
```


## anchorectl event

```text
Event related operations

Usage:
  anchorectl event [command]

Available Commands:
  delete      Delete an event by its ID or set of filters
  get         Lookup an event by its event ID
  list        Returns a paginated list of events in the descending order of their occurrence

Flags:
  -h, --help   help for event

Use "anchorectl event [command] --help" for more information about a command.

For help regarding global flags, run --help on the root command
```


### anchorectl event delete

```text
Delete an event by its event ID or set of filters

Usage:
  anchorectl event delete EVENT_ID [flags]

Arguments:
  EVENTID:  Id of event to delete

Aliases:
  delete, del

Flags:
      --all             delete all events
      --before string   delete events that occurred before the timestamp (env: ANCHORECTL_EVENT_BEFORE)
      --force           force without prompt (env: ANCHORECTL_EVENT_FORCE)
  -h, --help            help for delete
      --level string    delete events that match the level - INFO or ERROR (env: ANCHORECTL_EVENT_LEVEL)
  -o, --output string   the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")
      --since string    delete events that occurred after the timestamp (env: ANCHORECTL_EVENT_SINCE)

For help regarding global flags, run --help on the root command
```


### anchorectl event get

```text
Lookup an event by its event ID

Usage:
  anchorectl event get ID [flags]

Arguments:
  ID:  Event ID of the event for lookup

Flags:
  -h, --help            help for get
  -o, --output string   the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")

For help regarding global flags, run --help on the root command
```


### anchorectl event list

```text
Returns a paginated list of events in the descending order of their occurrence. Optional query parameters may be used for filtering results

Usage:
  anchorectl event list [flags]

Flags:
      --all                    return all events (env: ANCHORECTL_EVENT_ALL)
      --before string          return events that occurred before the ISO8601 formatted UTC timestamp
                               (env: ANCHORECTL_EVENT_BEFORE)
      --event-type string      filter events by a prefix match on the event type (e.g. "user.image.")
                               (env: ANCHORECTL_EVENT_TYPE)
  -h, --help                   help for list
      --host string            filter events by the originating host ID (env: ANCHORECTL_EVENT_SOURCE_HOST_ID)
      --level string           filter events by the level - INFO or ERROR (env: ANCHORECTL_EVENT_LEVEL)
  -o, --output string          the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")
      --page int32             return the nth page of results starting from 1. Defaults to first page if left empty
                               (env: ANCHORECTL_PAGE)
      --resource-id string     filter events by a specified resource ID (env: ANCHORECTL_EVENT_RESOURCE_ID)
      --resource-type string   filter events by the type of resource - tag, imageDigest, repository etc
                               (env: ANCHORECTL_EVENT_RESOURCE_TYPE)
      --service string         filter events by the originating service (env: ANCHORECTL_EVENT_SOURCE_SERVICE_NAME)
      --since string           return events that occurred after the ISO8601 formatted UTC timestamp
                               (env: ANCHORECTL_EVENT_SINCE)

For help regarding global flags, run --help on the root command
```


## anchorectl feed

```text
Feed related operations

Usage:
  anchorectl feed [command]

Available Commands:
  list        Return a list of feed and their groups along with update and record count information
  sync        Execute a synchronous update of all datasets from the anchore data service

Flags:
  -h, --help   help for feed

Use "anchorectl feed [command] --help" for more information about a command.

For help regarding global flags, run --help on the root command
```


### anchorectl feed list

```text
Return a list of feed and their groups along with update and record count information. This data reflects the state of the policy engine, not the upstream feed service itself.

Usage:
  anchorectl feed list [flags]

Flags:
  -h, --help            help for list
  -o, --output string   the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")

For help regarding global flags, run --help on the root command
```


### anchorectl feed sync

```text
Execute a synchronous update all the datasets. The response will block until complete.

Usage:
  anchorectl feed sync [flags]

Flags:
  -f, --force_sync      force the feed sync to occur (env: ANCHORECTL_FORCE_SYNC)
  -h, --help            help for sync
  -t, --timeout int32   the maximum time to wait for the feed sync to complete (env: ANCHORECTL_TIMEOUT) (default -1)

For help regarding global flags, run --help on the root command
```


## anchorectl image

```text
Image related operations

Usage:
  anchorectl image [command]

Available Commands:
  add             analyze a container image
  ancestors       Get image ancestors
  check           Get the policy evaluation for the given image
  content         Get image content
  delete          Delete an image analysis
  get             Get information about a single image
  list            List all images visible to the user
  metadata        Get image metadata
  sbom            Get image sbom in the native Anchore format
  vulnerabilities Get image vulnerabilities

Flags:
  -h, --help   help for image

Use "anchorectl image [command] --help" for more information about a command.

For help regarding global flags, run --help on the root command
```


### anchorectl image add

```text
analyze a container image

Usage:
  anchorectl image add [flags]


# Submit image for addition to Anchore Enterprise (Anchore Enterprise will pull
# image from registry and perform full analysis)

anchorectl image add ghcr.io/place/thing:v0.1.0

# Submit image for addition to Anchore Enterprise (anchorectl will perform full
# local image analysis, SBOM + additional analysis pushed to Anchore Enterprise)

anchorectl image add ghcr.io/place/thing:v0.1.0 --from docker

# Submit image for addition to Anchore Enterprise (use SBOM generated by Syft,
# no additional analysis performed, and push to Anchore Enterprise)

syft -o json ghcr.io/place/thing:v0.1.0 | anchorectl image add ghcr.io/place/thing:v0.1.0 --from -

# Submit and wait for analysis to complete

anchorectl image add ghcr.io/place/thing:v0.1.0 --wait

# Submit and get results once analysis is completed

anchorectl image add ghcr.io/place/thing:v0.1.0 --get content,vulnerabilities=/path/to/vulns.json

# Submit and fetch all results to a directory

anchorectl image add ghcr.io/place/thing:v0.1.0 --get all=/path/to/dir


Flags:
      --annotation stringArray   one or more key-value annotations to add on the image in anchore enterprise (format: key=value)
                                 (env: ANCHORECTL_IMAGE_ANNOTATION)
  -a, --application string       associate the image with an application at a specific version in the format 'app@version' (example: myapp@v3.1.4)
                                 (env: ANCHORECTL_APPLICATION)
  -d, --dockerfile string        path to the dockerfile for this image (env: ANCHORECTL_IMAGE_DOCKERFILE)
  -f, --force                    re-analyze the image even if it has already been analyzed (env: ANCHORECTL_FORCE)
      --from string              analyze from the given source (default: '', indicating that anchore enterprise will pull the image from the registry; allowable-values: <path-to-syft-SBOM>, -, docker, registry, docker-archive)
                                 (env: ANCHORECTL_IMAGE_FROM)
  -g, --get stringArray          get results and optionally write the raw results to a file (example: 'content' or 'content=./path/to/file.json' or 'all=/path/to/dir'; allowable-keys: image-metadata, sbom, sbomspdx, sbomcyclonedx, content, vulnerability, policy-evaluation, all)
                                 (env: ANCHORECTL_IMAGE_GET)
  -h, --help                     help for add
  -n, --no-auto-subscribe        do not automatically scan newly pushed tags to the registry for the given image
                                 (env: ANCHORECTL_IMAGE_NO_AUTO_SUBSCRIBE)
  -p, --platform string          an optional platform specifier for use with '--from registry' target type (e.g. 'linux/arm64', 'linux/arm64/v8', 'arm64', 'linux')
                                 (env: ANCHORECTL_IMAGE_PLATFORM)
  -w, --wait                     wait for the analysis to complete (env: ANCHORECTL_IMAGE_WAIT)

For help regarding global flags, run --help on the root command
```


### anchorectl image ancestors

```text
List analyzed ancestor images, which are the images that form the base layers of the image

Usage:
  anchorectl image ancestors IMAGE [flags]

Arguments:
  IMAGE:  the image to fetch the ancestors for (can be a digest, id, or registry/repo:tag)

Aliases:
  ancestors, ancestor

Flags:
  -b, --base            only show the analyzed ancestor image with the fewest layers (env: ANCHORECTL_ANCESTOR_BASE)
  -h, --help            help for ancestors
  -o, --output string   the format to show the results (allowable: [text json id]; env: ANCHORECTL_FORMAT) (default "text")
  -p, --parent          only show the analyzed ancestor image with the most layers (env: ANCHORECTL_ANCESTOR_PARENT)

For help regarding global flags, run --help on the root command
```


### anchorectl image check

```text
Get the policy evaluation for the given image

Usage:
  anchorectl image check IMAGE [flags]

Arguments:
  IMAGE:  The image to fetch the policy evaluation for (can be a digest, id or registry/repo:tag). If supplying a digest or image id, a tag must be supplied with the -t flag.

Aliases:
  check, evaluate

Flags:
      --detail                  show each failed gate within the policy evaluation report (env: ANCHORECTL_IMAGE_CHECK_DETAIL)
  -f, --fail-based-on-results   set the return code to 1 if the policy evaluation result shows as 'fail'
                                (env: ANCHORECTL_FAIL_BASED_ON_RESULTS)
  -h, --help                    help for check
      --history                 show all previous policy evaluations (env: ANCHORECTL_IMAGE_CHECK_HISTORY)
  -o, --output string           the format to show the results (allowable: [text json json-raw id csv]; env: ANCHORECTL_FORMAT) (default "text")
  -p, --policy string           the policy name or ID to evaluate against (if not provided the default policy is used)
                                (env: ANCHORECTL_POLICY)
  -t, --tag string              specify which tag (repo:tag) is evaluated for a given image ID or Image digest
                                (env: ANCHORECTL_IMAGE_TAG)

For help regarding global flags, run --help on the root command
```


### anchorectl image content

```text
Get image content

Usage:
  anchorectl image content IMAGE [flags]

Arguments:
  IMAGE:  The image ID, digest, or name:tag to fetch content of

Aliases:
  content, contents

Flags:
  -a, --available-types    only show available content types and exit (env: ANCHORECTL_AVAILABLE_TYPES)
      --file string        a file path to write a .tar file containing all retrieved files
                           (env: ANCHORECTL_FILE)
  -h, --help               help for content
  -o, --output string      the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")
      --overwrite          write over an existing file when saving retrieved files tarball
                           (env: ANCHORECTL_OVERWRITE)
  -t, --type stringArray   filter down results to one or more vulnerability types; use --available-types to see valid values (default: fetch all available types)
                           (env: ANCHORECTL_CONTENT_TYPES)

For help regarding global flags, run --help on the root command
```


### anchorectl image delete

```text
Delete an image analysis

Usage:
  anchorectl image delete IMAGE... [flags]

Arguments:
  IMAGE:  One or more images to delete (can be a digest, id or registry/repo:tag). If no tag supplied defaults to 'latest'

Aliases:
  delete, del

Flags:
  -a, --all             delete all images
  -f, --force           force deletion of image by cancelling any subscription/notification settings prior to image delete
                        (env: ANCHORECTL_IMAGE_DELETE_FORCE)
  -h, --help            help for delete
  -o, --output string   the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")

For help regarding global flags, run --help on the root command
```


### anchorectl image get

```text
Get information about a single image

Usage:
  anchorectl image get [flags]

Arguments:
  IMAGE:  the image ID, `name:tag`, `name@sha256:digest`, `name:tag@sha256:digest`, or `sha256:digest` value

Flags:
  -i, --digest string   the image digest (env: ANCHORECTL_IMAGE_DIGEST)
  -h, --help            help for get
      --history         show history of images that match the input image (env: ANCHORECTL_IMAGE_HISTORY)
  -o, --output string   the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")

For help regarding global flags, run --help on the root command
```


### anchorectl image list

```text
List all images visible to the user

Usage:
  anchorectl image list [flags]

Flags:
  -s, --analysis-status string   Filter by analysis_status value on the record. (allowable: [not_analyzed analyzed analyzing analysis_failed]; env: ANCHORECTL_IMAGE_ANALYSIS_STATUS)
  -h, --help                     help for list
      --history                  Include full history of images (duplicate tags with previous content)
                                 (env: ANCHORECTL_IMAGE_HISTORY)
  -i, --image string             Tag-based docker-pull string to filter results by (e.g. docker.io/library/nginx:latest, or myhost.com:5000/testimages:v1.1.1)
                                 (env: ANCHORECTL_IMAGE_NAME)
      --image-status string      Filter by "image_status" value on the record (allowable: [all active deleting]; env: ANCHORECTL_IMAGE_STATUS) (default "active")
  -o, --output string            the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")

For help regarding global flags, run --help on the root command
```


### anchorectl image metadata

```text
Get image metadata

Usage:
  anchorectl image metadata IMAGE [flags]

Arguments:
  IMAGE:  The image ID, digest, or name:tag to fetch metadata of

Flags:
      --file string   a file path to write the metadata out to (env: ANCHORECTL_FILE)
  -h, --help          help for metadata
      --overwrite     write over existing metadata files (env: ANCHORECTL_OVERWRITE)
  -t, --type string   filter down results to one or more vulnerability types (run command without this flag to see available types for the given image)
                      (env: ANCHORECTL_METADATA_TYPE)

For help regarding global flags, run --help on the root command
```


### anchorectl image sbom

```text
Get image sbom in the native Anchore format

Usage:
  anchorectl image sbom IMAGE [flags]

Arguments:
  IMAGE:  the image reference (ID, digest, name:tag)

Flags:
  -f, --file string     write the SBOM content to a file (instead of STDOUT) (env: ANCHORECTL_FILE)
  -h, --help            help for sbom
  -o, --output string   report output format, options=[cyclonedx-json cyclonedx-xml spdx-json spdx-tag-value syft-json table text] (default "syft-json")
      --overwrite       write over existing SBOM files (env: ANCHORECTL_OVERWRITE)

For help regarding global flags, run --help on the root command
```


### anchorectl image vulnerabilities

```text
Get image vulnerabilities

Usage:
  anchorectl image vulnerabilities IMAGE [flags]

Arguments:
  IMAGE:  The image ID, digest, or name:tag to fetch vulnerabilities for

Aliases:
  vulnerabilities, vulns, vuln

Flags:
  -a, --available-types            only show available vulnerability types and exit
  -h, --help                       help for vulnerabilities
      --include-description        Include full descriptions in the vulnerability result (env: ANCHORECTL_VULNERABILITY_INCLUDE_DESCRIPTION)
  -o, --output string              the format to show the results (allowable: [text json json-raw csv]; env: ANCHORECTL_FORMAT) (default "text")
  -r, --refresh                    refresh the vulnerability match results against the original artifact
                                   (env: ANCHORECTL_VULNERABILITY_REFRESH)
  -t, --type stringArray           filter down results to one or more vulnerability types (env: ANCHORECTL_VULNERABILITY_TYPE)
      --vendor-only will_not_fix   filter results to include only vulnerabilities that are not marked as invalid by upstream OS vendor data. When set to true, it will filter out all vulnerabilities where will_not_fix is False. If false all vulnerabilities are returned regardless of `will_not_fix`
                                   (env: ANCHORECTL_VULNERABILITY_VENDOR_ONLY)

For help regarding global flags, run --help on the root command
```


## anchorectl inventory

```text
Inventory list operation

Usage:
  anchorectl inventory [command]

Available Commands:
  delete      Delete inventory from the system
  list        Returns a list of the images that are in use
  watch       Inventory subscription operations

Flags:
  -h, --help   help for inventory

Use "anchorectl inventory [command] --help" for more information about a command.

For help regarding global flags, run --help on the root command
```


### anchorectl inventory delete

```text
Delete inventory from the system.

Usage:
  anchorectl inventory delete [flags]

Aliases:
  delete, del

Flags:
      --context string        The inventory context (env: ANCHORECTL_CONTEXT)
  -h, --help                  help for delete
      --image-digest string   The image digest to delete inventory for (env: ANCHORECTL_IMAGE_DIGEST)
  -o, --output string         the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")
      --type string           The type of inventory to delete (env: ANCHORECTL_INVENTORY_INVENTORY_TYPE)
  -y, --yes                   Confirm the deletion of the inventory (env: ANCHORECTL_CONFIRM)

For help regarding global flags, run --help on the root command
```


### anchorectl inventory list

```text
Returns a list of the images that are in use

Usage:
  anchorectl inventory list [flags]

Flags:
      --context string        Limit results to a specific image context (env: ANCHORECTL_INVENTORY_CONTEXT)
  -h, --help                  help for list
      --image-digest string   Search for a specific image digest (env: ANCHORECTL_INVENTORY_IMAGE_DIGEST)
  -o, --output string         the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")
      --type string           The inventory type to limit results (e.g. kubernetes) (env: ANCHORECTL_INVENTORY_TYPE)

For help regarding global flags, run --help on the root command
```


### anchorectl inventory watch

```text
Inventory subscription operations

Usage:
  anchorectl inventory watch [command]

Available Commands:
  activate    Watching a runtime inventory context will cause images to be automatically scheduled for analysis on discovery
  deactivate  Runtime inventory context to stop watching
  list        List all runtime inventory which have a watch configured

Flags:
  -h, --help   help for watch

Use "anchorectl inventory watch [command] --help" for more information about a command.

For help regarding global flags, run --help on the root command
```


#### anchorectl inventory watch activate

```text
Watching a runtime inventory context will cause images to be automatically scheduled for analysis on discovery

Usage:
  anchorectl inventory watch activate INVENTORY_CONTEXT [flags]

Arguments:
  INVENTORY_CONTEXT:  inventory context

Flags:
  -h, --help            help for activate
  -o, --output string   the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")

For help regarding global flags, run --help on the root command
```


#### anchorectl inventory watch deactivate

```text
Runtime inventory context to stop watching

Usage:
  anchorectl inventory watch deactivate INVENTORY_CONTEXT [flags]

Arguments:
  INVENTORY_CONTEXT:  runtime inventory context

Flags:
  -h, --help            help for deactivate
  -o, --output string   the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")

For help regarding global flags, run --help on the root command
```


#### anchorectl inventory watch list

```text
List all runtime inventory which have a watch configured

Usage:
  anchorectl inventory watch list [flags]

Flags:
  -h, --help            help for list
  -k, --key string      filter on this specific inventory context (env: ANCHORECTL_SUBSCRIPTION_KEY)
  -o, --output string   the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")

For help regarding global flags, run --help on the root command
```


## anchorectl policy

```text
Policy related operations

Usage:
  anchorectl policy [command]

Available Commands:
  activate    Activate a policy
  add         Adds a new policy bundle to the system
  delete      Delete the specified policy
  get         Get the policy bundle content
  list        List all saved policy bundles
  update      Update/replace an existing policy

Flags:
  -h, --help   help for policy

Use "anchorectl policy [command] --help" for more information about a command.

For help regarding global flags, run --help on the root command
```


### anchorectl policy activate

```text
Activate a policy

Usage:
  anchorectl policy activate POLICY [flags]

Arguments:
  POLICY:  The policy name or ID

Flags:
  -h, --help            help for activate
  -o, --output string   the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")

For help regarding global flags, run --help on the root command
```


### anchorectl policy add

```text
Adds a new policy bundle to the system

Usage:
  anchorectl policy add [flags]

Flags:
  -h, --help            help for add
  -i, --input string    path to a JSON input file or - to read from stdin (env: ANCHORECTL_INPUT)
  -o, --output string   the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")

For help regarding global flags, run --help on the root command
```


### anchorectl policy delete

```text
Delete the specified policy

Usage:
  anchorectl policy delete POLICY [flags]

Arguments:
  POLICY:  The policy name or ID

Aliases:
  delete, del

Flags:
  -h, --help            help for delete
  -o, --output string   the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")

For help regarding global flags, run --help on the root command
```


### anchorectl policy get

```text
Get the policy bundle content

Usage:
  anchorectl policy get POLICY [flags]

Arguments:
  POLICY:  the policy name or ID

Flags:
      --detail          include policy bundle detail in the form of the full bundle content for each entry
                        (env: ANCHORECTL_POLICY_DETAIL) (default true)
  -h, --help            help for get
  -o, --output string   the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")

For help regarding global flags, run --help on the root command
```


### anchorectl policy list

```text
List all saved policy bundles

Usage:
  anchorectl policy list [flags]

Flags:
      --detail          Include policy bundle detail in the form of the full bundle content for each entry
                        (env: ANCHORECTL_DETAIL) (default true)
  -h, --help            help for list
  -o, --output string   the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")

For help regarding global flags, run --help on the root command
```


### anchorectl policy update

```text
Update/replace an existing policy

Usage:
  anchorectl policy update [flags]

Flags:
  -h, --help            help for update
  -i, --input string    path to a JSON input file or - to read from stdin (env: ANCHORECTL_INPUT)
  -o, --output string   the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")

For help regarding global flags, run --help on the root command
```


## anchorectl registry

```text
Registry credential operations

Usage:
  anchorectl registry [command]

Available Commands:
  add         Adds a new registry to the system
  delete      Delete a registry configuration record from the system
  get         Get information on a specific registry
  list        List all configured registries the system can/will watch
  update      Replaces an existing registry record with the given record

Flags:
  -h, --help   help for registry

Use "anchorectl registry [command] --help" for more information about a command.

For help regarding global flags, run --help on the root command
```


### anchorectl registry add

```text
Adds a new registry to the system

Usage:
  anchorectl registry add REGISTRY [flags]

Arguments:
  REGISTRY:  hostname:port string for accessing the registry, as would be used in a docker pull operation. May include some or all of a repository and wildcards (e.g. docker.io/library/* or gcr.io/myproject/myrepository)

Flags:
  -h, --help                help for add
      --name string         human readable name associated with registry record (env: ANCHORECTL_REGISTRY_NAME)
  -o, --output string       the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")
      --secure-connection   Use TLS/SSL verification for the registry URL (env: ANCHORECTL_REGISTRY_SECURE_CONNECTION) (default true)
      --type string         Type of registry (env: ANCHORECTL_REGISTRY_TYPE) (default "docker_v2")
      --username string     Username portion of credential to use for this registry (env: ANCHORECTL_REGISTRY_USERNAME)
      --validate            whether or not to validate registry/credential at registry add time
                            (env: ANCHORECTL_REGISTRY_VALIDATE) (default true)

For help regarding global flags, run --help on the root command
```


### anchorectl registry delete

```text
Delete a registry configuration record from the system. Does not remove any images.

Usage:
  anchorectl registry delete REGISTRY [flags]

Arguments:
  REGISTRY:  the registry name

Aliases:
  delete, del

Flags:
  -h, --help            help for delete
  -o, --output string   the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")

For help regarding global flags, run --help on the root command
```


### anchorectl registry get

```text
Get information on a specific registry

Usage:
  anchorectl registry get REGISTRY [flags]

Arguments:
  REGISTRY:  registry name

Flags:
  -h, --help            help for get
  -o, --output string   the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")

For help regarding global flags, run --help on the root command
```


### anchorectl registry list

```text
List all configured registries the system can/will watch

Usage:
  anchorectl registry list [flags]

Flags:
  -h, --help            help for list
  -o, --output string   the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")

For help regarding global flags, run --help on the root command
```


### anchorectl registry update

```text
Replaces an existing registry record with the given record

Usage:
  anchorectl registry update REGISTRY [flags]

Arguments:
  REGISTRY:  the registry name

Flags:
  -h, --help                help for update
      --name string         human readable name associated with registry record (env: ANCHORECTL_REGISTRY_NAME)
  -o, --output string       the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")
      --secure-connection   Use TLS/SSL verification for the registry URL (env: ANCHORECTL_REGISTRY_SECURE_CONNECTION)
      --type string         Type of registry (env: ANCHORECTL_REGISTRY_TYPE)
      --username string     Username portion of credential to use for this registry (env: ANCHORECTL_REGISTRY_USERNAME)
      --validate            whether or not to validate registry/credential at registry update time
                            (env: ANCHORECTL_REGISTRY_VALIDATE) (default true)

For help regarding global flags, run --help on the root command
```


## anchorectl repo

```text
Repository related operations

Usage:
  anchorectl repo [command]

Available Commands:
  add         Add repository to watch
  delete      Delete a repository subscription
  get         Get a specific repository subscription
  list        List all repository subscriptions
  unwatch     Stop watching a specific repository
  watch       Start watching a specific repository

Flags:
  -h, --help   help for repo

Use "anchorectl repo [command] --help" for more information about a command.

For help regarding global flags, run --help on the root command
```


### anchorectl repo add

```text
Add repository to watch

Usage:
  anchorectl repo add REPOSITORY [flags]

Arguments:
  REPOSITORY:  full repository to add e.g. docker.io/library/alpine

Flags:
      --auto-subscribe          enable/disable auto tag_update activation when new images from a repo are added
                                (env: ANCHORECTL_REPO_AUTO_SUBSCRIBE)
      --dry-run                 return tags in the repository without actually watching the repository
                                (env: ANCHORECTL_REPO_DRY_RUN)
      --exclude-existing-tags   indicates if you want to ignore the existing tags in the repository on the first execution
                                (env: ANCHORECTL_REPO_EXCLUDE_EXISTING_TAGS)
  -h, --help                    help for add
  -o, --output string           the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")

For help regarding global flags, run --help on the root command
```


### anchorectl repo delete

```text
Delete a repository subscription

Usage:
  anchorectl repo delete REPOSITORY [flags]

Arguments:
  REPOSITORY:  full repository e.g. docker.io/library/alpine

Aliases:
  delete, del

Flags:
  -h, --help            help for delete
  -o, --output string   the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")

For help regarding global flags, run --help on the root command
```


### anchorectl repo get

```text
Get a specific repository subscription

Usage:
  anchorectl repo get REPOSITORY [flags]

Arguments:
  REPOSITORY:  full repository e.g. docker.io/library/alpine

Flags:
  -h, --help            help for get
  -o, --output string   the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")

For help regarding global flags, run --help on the root command
```


### anchorectl repo list

```text
List all repository subscriptions

Usage:
  anchorectl repo list [flags]

Flags:
  -h, --help                help for list
  -o, --output string       the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")
      --repository string   filter only subscriptions matching the repository (env: ANCHORECTL_REPOSITORY_NAME)

For help regarding global flags, run --help on the root command
```


### anchorectl repo unwatch

```text
Stop watching a specific repository

Usage:
  anchorectl repo unwatch REPOSITORY [flags]

Arguments:
  REPOSITORY:  full repository e.g. docker.io/library/alpine

Flags:
  -h, --help            help for unwatch
  -o, --output string   the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")

For help regarding global flags, run --help on the root command
```


### anchorectl repo watch

```text
Start watching a specific repository

Usage:
  anchorectl repo watch REPOSITORY [flags]

Arguments:
  REPOSITORY:  full repository e.g. docker.io/library/alpine

Flags:
  -h, --help            help for watch
  -o, --output string   the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")

For help regarding global flags, run --help on the root command
```


## anchorectl source

```text
Source repository related operations

Usage:
  anchorectl source [command]

Available Commands:
  add             Analyze a source repository (from an existing SBOM)
  check           Fetch or calculate policy evaluation for a source
  content         Get source content
  delete          Delete source record from DB
  get             Get a detailed source repository analysis metadata record
  list            List the source repository analysis records
  sbom            Retrieve the source sbom for the specified source
  vulnerabilities Get vulnerabilities for the source by type

Flags:
  -h, --help   help for source

Use "anchorectl source [command] --help" for more information about a command.

For help regarding global flags, run --help on the root command
```


### anchorectl source add

```text
Analyze a source repository (from an existing SBOM)

Usage:
  anchorectl source add [flags]

# Submit source SBOM for analysis by analyzers (don't wait for the results)
anchorectl source add github.com/my/repo@73522db08db1758c251ad714696d3120ac9b55f4 \
    --from ./path/to/sbom.json

# Submit source SBOM for analysis and wait for the analysis to complete
anchorectl source add github.com/my/repo@73522db08db1758c251ad714696d3120ac9b55f4 \
    --from ./path/to/sbom.json \
    --wait

# Submit source SBOM and get analysis results (some to stdout, others written to a file)
anchorectl source add github.com/my/repo@73522db08db1758c251ad714696d3120ac9b55f4 \
    --from ./path/to/sbom.json \
    --get content \
    --get vulnerabilities=/path/to/vulnerabilities.json

# Submit source SBOM and fetch all results to a directory
anchorectl source add github.com/my/repo@73522db08db1758c251ad714696d3120ac9b55f4 \
    --from ./path/to/sbom.json \
    --get all=/path/to/dir

# Submit source SBOM from stdin
syft -o json . | \
    anchorectl source add github.com/my/repo@73522db08db1758c251ad714696d3120ac9b55f4 \
        --from -


Flags:
  -a, --application string          associate the image with an application at a specific version in the format 'app@version' (example: myapp@v3.1.4)
      --author string               author of the incoming commit
  -b, --branch string               name of the source branch
  -f, --force                       re-analyze the image even if it has already been analyzed
      --from string                 analyze from the given source (allowable-values: <path-to-syft-SBOM>, -)
  -g, --get stringArray             get results and optionally write the raw results to a file (example: 'content' or 'content=./path/to/file.json' or 'all=/path/to/dir'; allowable-keys: source-metadata, sbom, content, vulnerability, policy-evaluation, all)
  -h, --help                        help for add
  -w, --wait                        wait for the analysis to complete
  -n, --workflow-name string        name of the CI workflow
  -t, --workflow-timestamp string   time the CI workflow ran

For help regarding global flags, run --help on the root command
```


### anchorectl source check

```text
Fetch or calculate policy evaluation for a source

Usage:
  anchorectl source check SOURCE [flags]

Arguments:
  SOURCE:  "host/repo@revision" or UUID of source to check

Flags:
  -f, --fail-based-on-results   set the return code to 1 if the policy evaluation result shows as 'fail'
                                (env: ANCHORECTL_FAIL_BASED_ON_RESULTS)
  -h, --help                    help for check
  -o, --output string           the format to show the results (allowable: [text json id csv]; env: ANCHORECTL_FORMAT) (default "text")
  -p, --policy string           the policy name or ID to evaluate against (if not provided the default policy is used)
                                (env: ANCHORECTL_POLICY)

For help regarding global flags, run --help on the root command
```


### anchorectl source content

```text
Get source content

Usage:
  anchorectl source content SOURCE [flags]

Arguments:
  SOURCE:  The 'host/repo@revision' or source UUID to fetch content for

Aliases:
  content, contents

Flags:
  -a, --available-types    only show available content types and exit
  -h, --help               help for content
  -o, --output string      the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")
  -t, --type stringArray   filter down results to one or more vulnerability types; use --available-types to see valid values (default: fetch all available types)

For help regarding global flags, run --help on the root command
```


### anchorectl source delete

```text
Delete source record from DB

Usage:
  anchorectl source delete SOURCE [flags]

Arguments:
  SOURCE:  "host/repo@revision" or UUID of source to delete

Aliases:
  delete, del

Flags:
      --force           force deletion (env: ANCHORECTL_SOURCE_DELETE_FORCE)
  -h, --help            help for delete
  -o, --output string   the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")

For help regarding global flags, run --help on the root command
```


### anchorectl source get

```text
Get a detailed source repository analysis metadata record

Usage:
  anchorectl source get SOURCE [flags]

Arguments:
  SOURCE:  "host/repo@revision" or UUID of source to fetch

Flags:
  -h, --help            help for get
  -o, --output string   the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")

For help regarding global flags, run --help on the root command
```


### anchorectl source list

```text
List the source repository analysis records

Usage:
  anchorectl source list [flags]

Flags:
  -h, --help            help for list
  -o, --output string   the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")

For help regarding global flags, run --help on the root command
```


### anchorectl source sbom

```text
Retrieve the source sbom for the specified source

Usage:
  anchorectl source sbom SOURCE [flags]

Arguments:
  SOURCE:  "host/repo@revision" or UUID of source to fetch

Flags:
  -f, --file string     write the SBOM content to a file (instead of STDOUT) (env: ANCHORECTL_SBOM_FILE)
  -h, --help            help for sbom
  -o, --output string   report output format, options=[cyclonedx-json cyclonedx-xml spdx-json spdx-tag-value syft-json table text] (default "syft-json")
      --overwrite       write over existing SBOM files (env: ANCHORECTL_SBOM_OVERWRITE)

For help regarding global flags, run --help on the root command
```


### anchorectl source vulnerabilities

```text
Get vulnerabilities for the source by type

Usage:
  anchorectl source vulnerabilities SOURCE [flags]

Arguments:
  SOURCE:  the host/repo@revision or UUID to match vulnerabilities against

Aliases:
  vulnerabilities, vulns, vuln

Flags:
  -a, --available-types       only show available vulnerability types and exit (env: ANCHORECTL_AVAILABLE_TYPES)
  -h, --help                  help for vulnerabilities
      --include-description   Include full descriptions in the vulnerability result (env: ANCHORECTL_VULNERABILITY_INCLUDE_DESCRIPTION)
  -o, --output string         the format to show the results (allowable: [text json id csv]; env: ANCHORECTL_FORMAT) (default "text")
      --refresh               refresh the vulnerability match results against the original artifact
                              (env: ANCHORECTL_REFRESH)
  -t, --type stringArray      filter down results to one or more vulnerability types (env: ANCHORECTL_VULNERABILITY_TYPE)
  -n, --will-not-fix          filter out vulnerabilities explicitly marked as will-not-fix if set
                              (env: ANCHORECTL_WILL_NOT_FIX)

For help regarding global flags, run --help on the root command
```


## anchorectl subscription

```text
Subscription related operations

Usage:
  anchorectl subscription [command]

Available Commands:
  activate    Activate an existing subscription
  deactivate  Deactivate an existing subscription
  delete      Delete a subscription
  get         Get a specific subscription
  list        List all subscriptions

Flags:
  -h, --help   help for subscription

Use "anchorectl subscription [command] --help" for more information about a command.

For help regarding global flags, run --help on the root command
```


### anchorectl subscription activate

```text
Activate an existing subscription

Usage:
  anchorectl subscription activate KEY TYPE [flags]

Arguments:
  KEY:  the subscription key
  TYPE:  the type of the subscription (e.g. tag_update, policy_eval, vuln_update, analysis_update, runtime_inventory)

Flags:
  -h, --help            help for activate
  -o, --output string   the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")

For help regarding global flags, run --help on the root command
```


### anchorectl subscription deactivate

```text
Deactivate an existing subscription

Usage:
  anchorectl subscription deactivate KEY TYPE [flags]

Arguments:
  KEY:  the subscription key
  TYPE:  the type of the subscription (e.g. tag_update, policy_eval, vuln_update, analysis_update, runtime_inventory)

Flags:
  -h, --help            help for deactivate
  -o, --output string   the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")

For help regarding global flags, run --help on the root command
```


### anchorectl subscription delete

```text
Delete a subscription

Usage:
  anchorectl subscription delete KEY TYPE [flags]

Arguments:
  KEY:  the subscription key
  TYPE:  the type of the subscription (e.g. tag_update, policy_eval, vuln_update, analysis_update)

Aliases:
  delete, del

Flags:
  -h, --help            help for delete
  -o, --output string   the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")

For help regarding global flags, run --help on the root command
```


### anchorectl subscription get

```text
Get a specific subscription

Usage:
  anchorectl subscription get KEY TYPE [flags]

Arguments:
  KEY:  the subscription key
  TYPE:  the type of the subscription (e.g. tag_update, policy_eval, vuln_update, analysis_update)

Flags:
  -h, --help            help for get
  -o, --output string   the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")

For help regarding global flags, run --help on the root command
```


### anchorectl subscription list

```text
List all subscriptions

Usage:
  anchorectl subscription list [flags]

Flags:
  -h, --help            help for list
  -k, --key string      filter only subscriptions matching key (env: ANCHORECTL_SUBSCRIPTION_KEY)
  -o, --output string   the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")
  -t, --type string     filter only subscriptions matching type (env: ANCHORECTL_SUBSCRIPTION_TYPE)

For help regarding global flags, run --help on the root command
```


## anchorectl system

```text
System related operations

Usage:
  anchorectl system [command]

Available Commands:
  artifact-lifecycle-policy Global artifact lifecycle policy operations
  delete                    Delete service
  integration               Product Integration Operations
  role                      RBAC Role Operations
  smoke-tests               Smoke test related operations
  status                    Get the system status
  wait                      Wait for configured anchore system to be running

Flags:
  -h, --help   help for system

Use "anchorectl system [command] --help" for more information about a command.

For help regarding global flags, run --help on the root command
```


## anchorectl user

```text
User related operations

Usage:
  anchorectl user [command]

Available Commands:
  add          Create a new user
  delete       Delete a specific user credential by username of the credential
  get          Get a specific user in the specified account
  list         List users for the account
  set-password Set the password for a user

Flags:
  -h, --help   help for user

Use "anchorectl user [command] --help" for more information about a command.

For help regarding global flags, run --help on the root command
```


### anchorectl user add

```text
Create a new user

Usage:
  anchorectl user add USERNAME [flags]

Arguments:
  USERNAME:  the name of the user to create

Flags:
      --account string     the account to use, defaults to current account (env: ANCHORECTL_USER_ACCOUNT)
  -h, --help               help for add
      --idp_name string    the name of the IDP user will be authenticated with (env: ANCHORECTL_IDP_NAME)
  -o, --output string      the format to show the results (allowable: [text json id]; env: ANCHORECTL_FORMAT) (default "text")
      --role stringArray   the initial role(s) for the user. Defaults to (read-write) when not in the admin account.
                           (env: ANCHORECTL_USER_ROLE)

For help regarding global flags, run --help on the root command
```


### anchorectl user delete

```text
Delete a specific user credential by username of the credential. Cannot be the credential used to authenticate the request.

Usage:
  anchorectl user delete USERNAME [flags]

Arguments:
  USERNAME:  Name of the user to delete

Aliases:
  delete, del

Flags:
      --account string   The account to use, defaults to current account (env: ANCHORECTL_USER_ACCOUNT)
  -h, --help             help for delete
  -o, --output string    the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")

For help regarding global flags, run --help on the root command
```


### anchorectl user get

```text
Get a specific user in the specified account

Usage:
  anchorectl user get USERNAME [flags]

Arguments:
  USERNAME:  Name of the user to fetch

Flags:
      --account string   The account to use, defaults to current account (env: ANCHORECTL_USER_ACCOUNT)
  -h, --help             help for get
  -o, --output string    the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")

For help regarding global flags, run --help on the root command
```


### anchorectl user list

```text
List users for the account

Usage:
  anchorectl user list [flags]

Flags:
      --account string   The account to use, defaults to current account (env: ANCHORECTL_USER_ACCOUNT)
  -h, --help             help for list
  -o, --output string    the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")

For help regarding global flags, run --help on the root command
```


## anchorectl usergroup

```text
User Group Management Operations

Usage:
  anchorectl usergroup [command]

Available Commands:
  add         Create a new user group
  delete      Delete a user group
  get         Get a user group
  list        List user groups
  role        User Group Role Operations
  update      Update a user group
  user        User Group User Operations

Flags:
  -h, --help   help for usergroup

Use "anchorectl usergroup [command] --help" for more information about a command.

For help regarding global flags, run --help on the root command
```


### anchorectl usergroup add

```text
Create a new user group

Usage:
  anchorectl usergroup add NAME [flags]

Arguments:
  NAME:  The name of the user group

Flags:
  -d, --description string   The description of the user group (env: ANCHORECTL_USERGROUPPOST_DESCRIPTION)
  -h, --help                 help for add
  -o, --output string        the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")

For help regarding global flags, run --help on the root command
```


### anchorectl usergroup delete

```text
Delete a user group

Usage:
  anchorectl usergroup delete USER_GROUP [flags]

Arguments:
  USER_GROUP:  The name or uuid of the user group

Aliases:
  delete, del

Flags:
  -h, --help            help for delete
  -o, --output string   the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")

For help regarding global flags, run --help on the root command
```


### anchorectl usergroup get

```text
Get a user group

Usage:
  anchorectl usergroup get USER_GROUP [flags]

Arguments:
  USER_GROUP:  The name or uuid of the user group

Flags:
  -h, --help            help for get
  -o, --output string   the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")

For help regarding global flags, run --help on the root command
```


### anchorectl usergroup list

```text
List user groups

Usage:
  anchorectl usergroup list [flags]

Flags:
  -a, --contains-account string   Filter the user groups to only those that contain the specified domain name
                                  (env: ANCHORECTL_USERGROUP_CONTAINS_ACCOUNT)
  -u, --contains-user string      Filter the user groups to only those that contain the specified user
                                  (env: ANCHORECTL_USERGROUP_CONTAINS_USER)
  -h, --help                      help for list
  -o, --output string             the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")
  -g, --user-group-name string    Filter results to match the specified user group name (env: ANCHORECTL_USERGROUP_USER_GROUP_NAME)

For help regarding global flags, run --help on the root command
```


### anchorectl usergroup role

```text
User Group Role Operations

Usage:
  anchorectl usergroup role [command]

Available Commands:
  add         Add domain name and role(s) to this user group
  delete      Remove domain name and role(s) from this user group
  list        List accounts and roles configured in this user group

Flags:
  -h, --help   help for role

Use "anchorectl usergroup role [command] --help" for more information about a command.

For help regarding global flags, run --help on the root command
```


#### anchorectl usergroup role add

```text
Add domain name and role(s) to this user group

Usage:
  anchorectl usergroup role add USER_GROUP DOMAIN_NAME [flags]

Arguments:
  DOMAIN_NAME:  The domain name
  USER_GROUP:  The name or uuid of the user group

Flags:
  -h, --help               help for add
  -i, --input string       path to a JSON input file or - to read from stdin (env: ANCHORECTL_INPUT)
  -o, --output string      the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")
  -r, --role stringArray   The RBAC role(s) that will be associated with the specified domain
                           (env: ANCHORECTL_ROLE)

For help regarding global flags, run --help on the root command
```


#### anchorectl usergroup role delete

```text
Remove domain name and role(s) from this user group

Usage:
  anchorectl usergroup role delete USER_GROUP DOMAIN_NAME [flags]

Arguments:
  DOMAIN_NAME:  The domain name
  USER_GROUP:  The name or uuid of the user group

Aliases:
  delete, del

Flags:
  -h, --help               help for delete
  -o, --output string      the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")
  -r, --role stringArray   The RBAC role(s) that will be associated with the specified domain name
                           (env: ANCHORECTL_ROLE)

For help regarding global flags, run --help on the root command
```


#### anchorectl usergroup role list

```text
List accounts and roles configured in this user group

Usage:
  anchorectl usergroup role list USER_GROUP [flags]

Arguments:
  USER_GROUP:  The name or uuid of the user group

Flags:
  -h, --help            help for list
  -i, --input string    path to a JSON input file or - to read from stdin (env: ANCHORECTL_INPUT)
  -o, --output string   the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")

For help regarding global flags, run --help on the root command
```


### anchorectl usergroup update

```text
Update a user group

Usage:
  anchorectl usergroup update USER_GROUP [flags]

Arguments:
  USER_GROUP:  The name or uuid of the user group

Flags:
  -d, --description string   The description of the user group (env: ANCHORECTL_USERGROUP_DESCRIPTION)
  -h, --help                 help for update
  -o, --output string        the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")

For help regarding global flags, run --help on the root command
```


### anchorectl usergroup user

```text
User Group User Operations

Usage:
  anchorectl usergroup user [command]

Available Commands:
  add         Add user(s) to this user group
  delete      Remove user(s) from this user group
  list        List users configured in this user group

Flags:
  -h, --help   help for user

Use "anchorectl usergroup user [command] --help" for more information about a command.

For help regarding global flags, run --help on the root command
```


#### anchorectl usergroup user add

```text
Add user(s) to this user group

Usage:
  anchorectl usergroup user add USER_GROUP [flags]

Arguments:
  USER_GROUP:  The name or uuid of the user group

Flags:
  -h, --help               help for add
  -i, --input string       path to a JSON input file or - to read from stdin (env: ANCHORECTL_INPUT)
  -o, --output string      the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")
  -u, --user stringArray   The username(s) that will be associated with the User Group (env: ANCHORECTL_USER)

For help regarding global flags, run --help on the root command
```


#### anchorectl usergroup user delete

```text
Remove user(s) from this user group

Usage:
  anchorectl usergroup user delete USER_GROUP [flags]

Arguments:
  USER_GROUP:  The name or uuid of the user group

Aliases:
  delete, del

Flags:
  -h, --help               help for delete
  -o, --output string      the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")
  -u, --user stringArray   The username(s) that will be removed from the User group (env: ANCHORECTL_USER)

For help regarding global flags, run --help on the root command
```


#### anchorectl usergroup user list

```text
List users configured in this user group

Usage:
  anchorectl usergroup user list USER_GROUP [flags]

Arguments:
  USER_GROUP:  The name or uuid of the user group

Flags:
  -h, --help            help for list
  -i, --input string    path to a JSON input file or - to read from stdin (env: ANCHORECTL_INPUT)
  -o, --output string   the format to show the results (allowable: [text json json-raw id]; env: ANCHORECTL_FORMAT) (default "text")

For help regarding global flags, run --help on the root command
```


## anchorectl version

```text
show anchorectl version information

Usage:
  anchorectl version [flags]

Flags:
  -h, --help            help for version
  -o, --output string   the format to show the results (allowable: [text json]) (default "text")

For help regarding global flags, run --help on the root command
```
