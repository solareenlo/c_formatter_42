# ############################################################################ #
#                                                                              #
#                                                         :::      ::::::::    #
#    align.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cacharle <me@cacharle.xyz>                 +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/10/04 09:56:31 by cacharle          #+#    #+#              #
#    Updated: 2021/10/14 16:46:27 by tayamamo         ###   ########.fr        #
#                                                                              #
# ############################################################################ #


import re
from enum import Enum

import c_formatter_42.formatters.helper as helper


class Scope(Enum):
    LOCAL = 0
    GLOBAL = 1


def align_scope(content: str, scope: Scope) -> str:
    """ Align content
        scope can be either local or global
          local:  for variable declarations in function
          global: for function prototypes
    """

    lines = content.split("\n")
    aligned = []
    # select regex according to scope
    if scope is Scope.LOCAL:
        align_regex = (
            "^\t"
            r"(?P<prefix>{type})\s+"
            r"(?P<suffix>\**({decl}|{decl} = .+);)$"
        )
    elif scope is Scope.GLOBAL:
        align_regex = (
            r"^(?P<prefix>{type})\s+"
            r"(?P<suffix>({name}\(.*\)?;?)|({decl}(;|(\s+=\s+.*))))$"
        )
    align_regex = align_regex.format(
        type=helper.REGEX_TYPE,
        name=helper.REGEX_NAME,
        decl=helper.REGEX_DECL_NAME
    )
    # get the lines to be aligned
    matches = [re.match(align_regex, line) for line in lines]
    aligned = [(i, match.group("prefix"), match.group("suffix"))
               for i, match in enumerate(matches)
               if match is not None and
               match.group("prefix") not in ["struct", "union", "enum"]]

    # global type declaration (struct/union/enum)
    if scope is Scope.GLOBAL:
        typedecl_open_regex = (r"^(?P<prefix>\s*(typedef\s+)?(struct|enum|union))"
                               r"\s*(?P<suffix>[a-zA-Z_]\w+)?$")
        typedecl_close_regex = r"^(?P<prefix>\})\s*(?P<suffix>([a-zA-Z_]\w+)?;)$"
        for i, line in enumerate(lines):
            m = re.match(typedecl_open_regex, line)
            if m is not None:
                if m.group("suffix") is not None:
                    aligned.append((i, m.group("prefix"), m.group("suffix")))
                continue
            m = re.match(typedecl_close_regex, line)
            if m is not None:
                if line != "};":
                    aligned.append((i, m.group("prefix"), m.group("suffix")))
                continue

    # get the minimum alignment required for each line
    min_alignment = max(
        (len(prefix.replace("\t", " " * 4)) // 4 + 1 for _, prefix, _ in aligned),
        default=1
    )
    for i, prefix, suffix in aligned:
        if scope is Scope.GLOBAL:
            if "struct" not in prefix and "enum" not in prefix and "union" not in prefix:
                lines[i] = prefix + "\t" + suffix
            else:
                lines[i] = prefix + " " + suffix
        if scope is Scope.LOCAL:
            alignment = len(prefix.replace("\t", " " * 4)) // 4
            lines[i] = prefix + "\t" * (min_alignment - alignment) + suffix
            lines[i] = "\t" + lines[i]
    return "\n".join(lines)


@helper.locally_scoped
def align_local(content: str) -> str:
    """ Wrapper for align_scope to use local_scope decorator """
    return align_scope(content, scope=Scope.LOCAL)


@helper.locally_scoped_struct
def align_local_struct(content: str) -> str:
    """ Wrapper for align_scope to use local_scope decorator """
    return align_scope(content, scope=Scope.LOCAL)


def align(content: str) -> str:
    """ Align the content in global and local scopes """
    content = align_scope(content, scope=Scope.GLOBAL)
    content = align_local(content)
    content = align_local_struct(content)
    return content
