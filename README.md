# [Insert App Name]

Something combining elements of GitHub Issues, Discord, and other similar apps.


<!-- ## Application Entity Comparisons

| this app         | discord   | github issues |
| ---              | ---       | ---           |
| `Org`            | `-`       | `Orgaization` |
| `Space`          | `Server`  | `Project`     |
| `SpaceMember`    | `User`    | `User`
| `User`           | `User`    | `User`
| `Issue`          | `Channel` |
| `Issue Comment`  | `Message` | -->

## Application Entities

### `User`

An authenticated user.


### `Org`

A collection of [`Space`](#space)s

Can be _public_ or _private_.


### `OrgMember`

Links a [`User`](#user) to an [`Org`](#org).


### `Space`

A collection [`Issue`](#issue)s.

Can be _public_ or _private_.


### `SpaceMember`

Links a [`User`](#user) to a [`Space`](#space).


### `Issue`

A thread of [`IssueComment`](#issuecomment)s.


### `IssueComment`

A body of text within which [`User`](#user)s, or other `IssueComment`s or [`Issue`](#issue)s may be referenced/linked.